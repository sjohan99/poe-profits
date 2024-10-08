from typing import Container, Iterable
from cachetools import TTLCache, cached
from fastapi import APIRouter
from poe_profit_calc.harvest import (
    calculate_profits,
    parse_orbs,
    parse_catalysts,
    PrimalCrystallisedLifeforce,
    VividCrystallisedLifeforce,
    PRIMAL_LIFEFORCE_PER_ORB_REROLL,
    VIVID_LIFEFORCE_PER_CATALYST_REROLL,
    RerollableItem,
)
from poe_profit_calc.items import Item
from poe_profit_calc.setup.setup import App
from poe_profit_calc.sources import PoeNinjaSource
from pydantic import BaseModel

router = APIRouter(
    prefix="/harvest",
)

price_fetcher = App.get_instance().price_fetcher


class RerollItemData(BaseModel):
    name: str
    chaos_value: float
    icon: str | None = None
    reroll_weight: int = 0
    expected_reroll_profit: float
    lifeforce_per_reroll: int

    @staticmethod
    def from_rerollable_item(item: RerollableItem, profit: float, lifeforce_per_reroll: int):
        return RerollItemData(
            name=item.name,
            chaos_value=item.chaos_value,
            icon=item.icon,
            reroll_weight=item.reroll_weight,
            expected_reroll_profit=profit,
            lifeforce_per_reroll=lifeforce_per_reroll,
        )


class Lifeforce(BaseModel):
    name: str
    chaos_value: float
    icon: str | None = None

    @staticmethod
    def from_item(lifeforce: Item):
        return Lifeforce(
            name=lifeforce.name,
            chaos_value=lifeforce.price,
            icon=lifeforce.img,
        )


class RerollSummary(BaseModel):
    items: list[RerollItemData]
    lifeforce: Lifeforce
    total_weight: int


class HarvestOverview(BaseModel):
    orbs: RerollSummary
    catalysts: RerollSummary


def create_summary(
    items: Iterable[RerollableItem], lifeforce: Item, lifeforce_amount: int
) -> RerollSummary:
    items = set(items)
    profits = calculate_profits(items, lifeforce.price, lifeforce_amount)
    item_data = [
        RerollItemData.from_rerollable_item(item, profit, lifeforce_amount)
        for item, profit in profits.items()
    ]
    item_data.sort(key=lambda x: x.expected_reroll_profit, reverse=True)
    lifeforce_data = Lifeforce.from_item(lifeforce)
    total_weight = sum([item.reroll_weight for item in items])
    return RerollSummary(items=item_data, lifeforce=lifeforce_data, total_weight=total_weight)


@router.get("/orbs")
@cached(cache=TTLCache(maxsize=128, ttl=1800))
def get_orb_summary() -> RerollSummary:
    primal_lifeforce = PrimalCrystallisedLifeforce
    price_fetcher.price_items({primal_lifeforce})
    raw_data = price_fetcher.get_raw_endpoint(PoeNinjaSource.DELIRIUM_ORB)
    parsed_data = parse_orbs(raw_data)
    return create_summary(parsed_data, primal_lifeforce, PRIMAL_LIFEFORCE_PER_ORB_REROLL)


@router.get("/catalysts")
@cached(cache=TTLCache(maxsize=128, ttl=1800))
def get_catalyst_summary() -> RerollSummary:
    primal_lifeforce = VividCrystallisedLifeforce
    price_fetcher.price_items({primal_lifeforce})
    raw_data = price_fetcher.get_raw_endpoint(PoeNinjaSource.CURRENCY)
    parsed_data = parse_catalysts(raw_data)
    return create_summary(parsed_data, primal_lifeforce, VIVID_LIFEFORCE_PER_CATALYST_REROLL)


@router.get("/overview")
@cached(cache=TTLCache(maxsize=128, ttl=1800))
def get_overview() -> HarvestOverview:
    primal_lifeforce = PrimalCrystallisedLifeforce
    vivid_lifeforce = VividCrystallisedLifeforce
    price_fetcher.price_items({primal_lifeforce, vivid_lifeforce})
    orb_data = price_fetcher.get_raw_endpoint(PoeNinjaSource.DELIRIUM_ORB)
    currency_data = price_fetcher.get_raw_endpoint(PoeNinjaSource.CURRENCY)
    orbs = parse_orbs(orb_data)
    catalysts = parse_catalysts(currency_data)
    orb_summary = create_summary(orbs, primal_lifeforce, PRIMAL_LIFEFORCE_PER_ORB_REROLL)
    catalyst_summary = create_summary(
        catalysts, vivid_lifeforce, VIVID_LIFEFORCE_PER_CATALYST_REROLL
    )
    return HarvestOverview(orbs=orb_summary, catalysts=catalyst_summary)
