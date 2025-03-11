from enum import Enum
from typing import Set, Tuple
from cachetools import TTLCache, cached
from poe_profit_calc.bossing.bosses import *
from poe_profit_calc.globals import League
from poe_profit_calc.setup.setup import App
from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter(
    prefix="/bosses",
)

price_fetchers = App.get_instance().price_fetchers


class BossId(str, Enum):
    the_searing_exarch = "the_searing_exarch"
    the_searing_exarch_uber = "the_searing_exarch_uber"
    the_eater_of_worlds = "the_eater_of_worlds"
    the_eater_of_worlds_uber = "the_eater_of_worlds_uber"
    the_shaper = "the_shaper"
    the_shaper_uber = "the_shaper_uber"
    the_elder = "the_elder"
    the_elder_uber = "the_elder_uber"
    the_elder_uber_uber = "the_elder_uber_uber"
    sirus = "sirus"
    sirus_uber = "sirus_uber"
    the_maven = "the_maven"
    the_maven_uber = "the_maven_uber"
    venarius = "venarius"
    venarius_uber = "venarius_uber"


BOSS_ID_TO_BOSS: dict[BossId, Boss] = {
    BossId.the_searing_exarch: TheSearingExarch,
    BossId.the_searing_exarch_uber: TheSearingExarchUber,
    BossId.the_eater_of_worlds: TheEaterOfWorlds,
    BossId.the_eater_of_worlds_uber: TheEaterOfWorldsUber,
    BossId.the_shaper: TheShaper,
    BossId.the_shaper_uber: TheShaperUber,
    BossId.the_elder: TheElder,
    BossId.the_elder_uber: TheElderUber,
    BossId.the_elder_uber_uber: TheElderUberUber,
    BossId.sirus: Sirus,
    BossId.sirus_uber: SirusUber,
    BossId.the_maven: TheMaven,
    BossId.the_maven_uber: TheMavenUber,
    BossId.venarius: Venarius,
    BossId.venarius_uber: VenariusUber,
}


class Drop(BaseModel):
    name: str
    price: float
    droprate: float
    reliable: bool
    trade_link: str | None
    img: str | None

    @staticmethod
    def from_item(item: Item, league: League):
        return Drop(
            name=item.name,
            price=item.price,
            droprate=item.droprate,
            reliable=item.reliable,
            trade_link=item.trade_link.get_link(league) if item.trade_link else None,
            img=item.img,
        )


class EntranceCost(BaseModel):
    name: str
    price: float
    quantity: int
    img: str | None

    @staticmethod
    def from_item(item: Item, quantity: int):
        return EntranceCost(
            name=item.name,
            price=item.price,
            quantity=quantity,
            img=item.img,
        )


class BossData(BaseModel):
    name: str
    short_name: str
    id: BossId
    drops: list[Drop]
    entrance_items: list[EntranceCost]

    @staticmethod
    def from_boss_id(boss_id: BossId, items: set[Item], league: League):
        drops = {item for item in items if item in BOSS_ID_TO_BOSS[boss_id].drops}
        entrance_items = set()
        for item in items:
            if item in BOSS_ID_TO_BOSS[boss_id].entrance_items:
                quantity = BOSS_ID_TO_BOSS[boss_id].entrance_items[item]
                entrance_items.add((item, quantity))
        id, boss = boss_id.value, BOSS_ID_TO_BOSS[boss_id]

        return BossData(
            name=boss.name,
            short_name=boss.short_name,
            id=boss_id,
            drops=[Drop.from_item(item, league) for item in drops],
            entrance_items=[
                EntranceCost.from_item(item, quantity) for item, quantity in entrance_items
            ],
        )


class BossSummary(BaseModel):
    name: str
    short_name: str
    id: BossId
    value: float
    reliable: bool
    img: str | None


@router.get("/boss/{boss_id}")
def get_boss_data(boss_id: BossId, league: League) -> BossData:
    boss_data = BOSS_ID_TO_BOSS[boss_id]
    items = price_fetchers[league].price_items(boss_data.items())
    return BossData.from_boss_id(boss_id, items, league)


@router.get("/all")
@cached(cache=TTLCache(maxsize=128, ttl=1800))
def get_bosses(league: League) -> list[BossData]:
    all_item_sets = [boss.items() for boss in BOSS_ID_TO_BOSS.values()]
    all_items = set.union(*all_item_sets)
    priced_items = price_fetchers[league].price_items(all_items)
    return [BossData.from_boss_id(boss, priced_items, league) for boss in BOSS_ID_TO_BOSS.keys()]


@router.get("/summary")
@cached(cache=TTLCache(maxsize=128, ttl=1800))
def get_summary(league: League) -> list[BossSummary]:
    summaries: list[BossSummary] = []
    all_item_sets = [boss.items() for boss in BOSS_ID_TO_BOSS.values()]
    all_items = set.union(*all_item_sets)
    priced_items = price_fetchers[league].price_items(all_items)
    for boss_id, boss in BOSS_ID_TO_BOSS.items():
        drops = {item for item in priced_items if item in boss.drops}
        entrance_items: Set[Tuple[Item, int]] = set()
        for item in priced_items:
            if item in boss.entrance_items:
                quantity = boss.entrance_items[item]
                entrance_items.add((item, quantity))

        value = 0
        value += sum(item.price * item.droprate for item in drops)
        value -= sum(item.price * quantity for item, quantity in entrance_items)

        img = None if not entrance_items else entrance_items.pop()[0].img
        summaries.append(
            BossSummary(
                name=boss.name,
                short_name=boss.short_name,
                id=boss_id,
                value=value,
                reliable=all(item.reliable for item in boss.items()),
                img=img,
            )
        )
    summaries.sort(key=lambda x: x.value, reverse=True)
    return summaries
