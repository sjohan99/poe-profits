from collections import Counter, defaultdict
from dataclasses import dataclass
from enum import Enum
from typing import Iterable
from poe_profit_calc.bossing import (
    Boss,
    BossItem,
    Sirus,
    SirusUber,
    TheEaterOfWorlds,
    TheEaterOfWorldsUber,
    TheElder,
    TheElderUber,
    TheElderUberUber,
    TheMaven,
    TheMavenUber,
    TheSearingExarch,
    TheSearingExarchUber,
    TheShaper,
    TheShaperUber,
    Venarius,
    VenariusUber,
    IncarnationOfNeglect,
    IncarnationOfFear,
    IncarnationOfDread,
    CatarinaMasterOfUndeath,
    TheKingInTheMists,
)
from pydantic import BaseModel
from fastapi import APIRouter
from poe_profit_calc.globals import League
from poe_profit_calc.setup.setup import App
from poe_profit_calc.vendor.request import PoeEndpoint
from .handler import PricedBossItem, get_parser_and_matcher


router = APIRouter(
    prefix="/bosses",
)

client = App.get_instance().client


class BossId(Enum):
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
    incarnation_of_dread = "incarnation_of_dread"
    incarnation_of_fear = "incarnation_of_fear"
    incarnation_of_neglect = "incarnation_of_neglect"
    catarina_master_of_undeath = "catarina_master_of_undeath"
    the_king_in_the_mists = "the_king_in_the_mists"


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
    BossId.incarnation_of_dread: IncarnationOfDread,
    BossId.incarnation_of_fear: IncarnationOfFear,
    BossId.incarnation_of_neglect: IncarnationOfNeglect,
    BossId.catarina_master_of_undeath: CatarinaMasterOfUndeath,
    BossId.the_king_in_the_mists: TheKingInTheMists,
}


def group_items_by_source(items: Iterable[BossItem]) -> dict[PoeEndpoint, list[BossItem]]:
    grouped_items = defaultdict(list)
    for item in items:
        grouped_items[item.matcher.source].append(item)
    return grouped_items


async def price_items(items: Iterable[BossItem], league: League) -> dict[BossItem, PricedBossItem]:
    assert items, "Items must not be empty"
    items_by_group = group_items_by_source(items)
    priced_items = {}
    endpoints = set(item.matcher.source for item in items)
    res = await client.request_endpoints(endpoints, league)
    for ep, data in res.items():
        if data is None:
            no_data_items = [item for item in items if item.matcher.source == ep]
            priced_items.update({item: PricedBossItem.not_found(item) for item in no_data_items})
            continue
        items_in_ep_group = items_by_group.get(ep, [])
        parser, matcher = get_parser_and_matcher(ep)
        parsed_data = parser(data)
        priced_items.update(matcher(parsed_data, items_in_ep_group))  # type: ignore
    return priced_items


@dataclass(frozen=True)
class PricedBoss:
    name: str
    short_name: str
    entrance_items: dict[PricedBossItem, int]
    drops: set[PricedBossItem]

    @staticmethod
    def from_boss(boss: Boss, priced_items: dict[BossItem, PricedBossItem]):
        entrance_items = {}
        drops = set()
        for item in boss.entrance_items:
            if item in priced_items:
                priced_item = priced_items[item]
                quantity = boss.entrance_items[item]
                entrance_items[priced_item] = quantity
        for item in boss.drops:
            if item in priced_items:
                drops.add(priced_items[item])
        assert len(entrance_items) == len(
            boss.entrance_items
        ), f"Not all entrance items were priced for {boss.name}"
        assert len(drops) == len(boss.drops), f"Not all drops were priced for {boss.name}"
        return PricedBoss(
            name=boss.name,
            short_name=boss.short_name,
            entrance_items=entrance_items,
            drops=drops,
        )

    def items(self) -> set[PricedBossItem]:
        return self.drops.union(set(self.entrance_items))


class Drop(BaseModel):
    name: str
    price: float
    droprate: float
    reliable: bool
    trade_link: str | None = None  # TODO: remove this attribute
    img: str | None
    found: bool

    @staticmethod
    def from_item(item: PricedBossItem):
        return Drop(
            name=item.boss_item.name,
            price=item.price,
            droprate=item.boss_item.drop_chance,
            reliable=item.reliable,
            trade_link=None,  # TODO: remove this attribute
            img=item.img,
            found=item.found,
        )


class EntranceCost(BaseModel):
    name: str
    price: float
    quantity: int
    img: str | None
    found: bool

    @staticmethod
    def from_item(item: PricedBossItem, quantity: int):
        return EntranceCost(
            name=item.boss_item.name,
            price=item.price,
            quantity=quantity,
            img=item.img,
            found=item.found,
        )


class BossData(BaseModel):
    name: str
    short_name: str
    id: BossId
    drops: list[Drop]
    entrance_items: list[EntranceCost]

    @staticmethod
    def from_priced_boss(priced_boss: PricedBoss, boss_id: BossId):
        drops = [Drop.from_item(item) for item in priced_boss.drops]
        entrance_items = [
            EntranceCost.from_item(item, quantity)
            for item, quantity in priced_boss.entrance_items.items()
        ]
        return BossData(
            name=priced_boss.name,
            short_name=priced_boss.short_name,
            id=boss_id,
            drops=drops,
            entrance_items=entrance_items,
        )


class BossSummary(BaseModel):
    name: str
    short_name: str
    id: BossId
    value: float
    reliable: bool
    img: str | None
    n_items_not_found: int


@router.get("/boss/{boss_id}")
async def get_boss_with_priced_items(boss_id: BossId, league: League):
    boss = BOSS_ID_TO_BOSS[boss_id]
    priced_items = await price_items(boss.items(), league)
    priced_boss = PricedBoss.from_boss(boss, priced_items)
    return BossData.from_priced_boss(priced_boss, boss_id)


@router.get("/all")
async def get_all_bosses(league: League) -> list[BossData]:
    all_item_sets = [boss.items() for boss in BOSS_ID_TO_BOSS.values()]
    all_items = set.union(*all_item_sets)
    priced_items = await price_items(all_items, league)
    response = []
    for boss_id, boss in BOSS_ID_TO_BOSS.items():
        priced_boss = PricedBoss.from_boss(boss, priced_items)
        response.append(BossData.from_priced_boss(priced_boss, boss_id))
    return response


@router.get("/summary")
async def get_summary(league: League) -> list[BossSummary]:
    summaries: list[BossSummary] = []
    all_item_sets = [boss.items() for boss in BOSS_ID_TO_BOSS.values()]
    all_items = set.union(*all_item_sets)
    priced_items = priced_items = await price_items(all_items, league)
    for boss_id, boss in BOSS_ID_TO_BOSS.items():
        priced_boss = PricedBoss.from_boss(boss, priced_items)
        drops = priced_boss.drops
        entrance_items = priced_boss.entrance_items
        value = 0
        value += sum(item.price * item.boss_item.drop_chance for item in drops)
        value -= sum(item.price * quantity for item, quantity in entrance_items.items())
        boss_items = drops.union(set(entrance_items.keys()))
        reliable = all(item.reliable for item in boss_items)

        # Exclude keys because they are almost never priced
        item_counter = Counter(
            item.found
            for item in (
                boss_item for boss_item in boss_items if " Key" not in boss_item.boss_item.name
            )
        )
        not_found_count = item_counter[False]

        sorted_entrance_items = sorted(
            list(entrance_items.items()), key=lambda x: x[0].boss_item.name
        )
        img = None if not entrance_items else sorted_entrance_items[0][0].img
        summaries.append(
            BossSummary(
                name=boss.name,
                short_name=boss.short_name,
                id=boss_id,
                value=value,
                reliable=reliable,
                img=img,
                n_items_not_found=not_found_count,
            )
        )
    summaries.sort(key=lambda x: x.value, reverse=True)
    return summaries
