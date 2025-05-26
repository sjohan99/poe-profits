import logging
from typing import Iterable
from fastapi import APIRouter
from poe_profit_calc.fetch import (
    PoeNinjaEndpoint,
    PoeNinjaCurrencyOverview,
    PoeNinjaCurrency,
    create_parser,
)
from poe_profit_calc.globals import League
from poe_profit_calc.harvest import (
    calculate_profits,
    parse_orbs,
    parse_catalysts,
    PRIMAL_LIFEFORCE_PER_ORB_REROLL,
    VIVID_LIFEFORCE_PER_CATALYST_REROLL,
    RerollableItem,
)

from poe_profit_calc.setup.setup import App
from poe_profit_calc.utils import find
from pydantic import BaseModel

VIVID_LIFEFORCE_NAME = "Vivid Crystallised Lifeforce"
PRIMAL_LIFEFORCE_NAME = "Primal Crystallised Lifeforce"

router = APIRouter(
    prefix="/harvest",
)

client = App.get_instance().client


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
    def from_item(lifeforce: PoeNinjaCurrency):
        return Lifeforce(
            name=lifeforce.name,
            chaos_value=lifeforce.receive.value,
            icon=lifeforce.icon,
        )

    @staticmethod
    def not_found(name: str):
        return Lifeforce(
            name=name,
            chaos_value=0,
            icon=None,
        )


class RerollSummary(BaseModel):
    items: list[RerollItemData]
    lifeforce: Lifeforce
    total_weight: int

    @staticmethod
    def create(items: Iterable[RerollableItem], lifeforce: Lifeforce, lifeforce_amount: int):
        items = set(items)
        profits = calculate_profits(items, lifeforce.chaos_value, lifeforce_amount)
        item_data = [
            RerollItemData.from_rerollable_item(item, profit, lifeforce_amount)
            for item, profit in profits.items()
        ]
        item_data.sort(key=lambda x: x.expected_reroll_profit, reverse=True)
        total_weight = sum([item.reroll_weight for item in items])
        return RerollSummary(items=item_data, lifeforce=lifeforce, total_weight=total_weight)


class HarvestOverview(BaseModel):
    orbs: RerollSummary
    catalysts: RerollSummary

    @staticmethod
    def from_summaries(orb_summary: RerollSummary | None, catalyst_summary: RerollSummary | None):
        if orb_summary is None:
            orb_summary = RerollSummary.create([], Lifeforce.not_found(PRIMAL_LIFEFORCE_NAME), 0)
        if catalyst_summary is None:
            catalyst_summary = RerollSummary.create(
                [], Lifeforce.not_found(VIVID_LIFEFORCE_NAME), 0
            )
        return HarvestOverview(
            orbs=orb_summary,
            catalysts=catalyst_summary,
        )


def get_lifeforce_from_data(data: bytes, lifeforce_name: str, league: League) -> Lifeforce:
    primal_lifeforce_cost = create_parser(PoeNinjaCurrencyOverview)(data)
    if not primal_lifeforce_cost:
        return Lifeforce.not_found(lifeforce_name)
    lifeforce_item = find(primal_lifeforce_cost.lines, lambda x: x.name == lifeforce_name)
    if lifeforce_item is None:
        logging.warning(f"{lifeforce_name} not found in 'poe.ninja' data for league '{league}'.")
        return Lifeforce.not_found(lifeforce_name)
    lifeforce = Lifeforce.from_item(lifeforce_item)
    if lifeforce.chaos_value == 0:
        logging.warning(f"{lifeforce_name} cost is 0 in league '{league}'.")
    return lifeforce


@router.get("/orbs")
async def get_orb_summary(league: League) -> RerollSummary:
    raw_data = await client.request_endpoints(
        [PoeNinjaEndpoint.DELIRIUM_ORB, PoeNinjaEndpoint.CURRENCY], league
    )
    orb_data = raw_data.get(PoeNinjaEndpoint.DELIRIUM_ORB)
    currency_data = raw_data.get(PoeNinjaEndpoint.CURRENCY)
    if orb_data is None or currency_data is None:
        return RerollSummary.create(
            [],
            Lifeforce.not_found(PRIMAL_LIFEFORCE_NAME),
            0,
        )
    parsed_orb_data = parse_orbs(orb_data) if orb_data else set()
    lifeforce = get_lifeforce_from_data(currency_data, PRIMAL_LIFEFORCE_NAME, league)
    return RerollSummary.create(parsed_orb_data, lifeforce, PRIMAL_LIFEFORCE_PER_ORB_REROLL)


@router.get("/catalysts")
async def get_catalyst_summary(league: League) -> RerollSummary:
    raw_data = await client.request_endpoint(
        PoeNinjaEndpoint.CURRENCY,
        league,
    )
    if raw_data is None:
        return RerollSummary.create(
            [],
            Lifeforce.not_found(VIVID_LIFEFORCE_NAME),
            0,
        )
    parsed_catalyst_data = parse_catalysts(raw_data)
    lifeforce = get_lifeforce_from_data(raw_data, VIVID_LIFEFORCE_NAME, league)
    return RerollSummary.create(
        parsed_catalyst_data, lifeforce, VIVID_LIFEFORCE_PER_CATALYST_REROLL
    )


@router.get("/overview")
async def get_overview(league: League) -> HarvestOverview:
    raw_data = await client.request_endpoints(
        [PoeNinjaEndpoint.DELIRIUM_ORB, PoeNinjaEndpoint.CURRENCY], league
    )
    orb_data = raw_data.get(PoeNinjaEndpoint.DELIRIUM_ORB)
    currency_data = raw_data.get(PoeNinjaEndpoint.CURRENCY)
    if currency_data is None:
        return HarvestOverview.from_summaries(None, None)
    primal_lifeforce = get_lifeforce_from_data(currency_data, PRIMAL_LIFEFORCE_NAME, league)
    vivid_lifeforce = get_lifeforce_from_data(currency_data, VIVID_LIFEFORCE_NAME, league)
    catalyst_summary = RerollSummary.create(
        parse_catalysts(currency_data), vivid_lifeforce, VIVID_LIFEFORCE_PER_CATALYST_REROLL
    )
    if orb_data is None:
        return HarvestOverview.from_summaries(
            None,
            catalyst_summary,
        )
    return HarvestOverview(
        orbs=RerollSummary.create(
            parse_orbs(orb_data), primal_lifeforce, PRIMAL_LIFEFORCE_PER_ORB_REROLL
        ),
        catalysts=catalyst_summary,
    )
