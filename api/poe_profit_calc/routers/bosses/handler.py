from dataclasses import dataclass
from typing import Iterable
from poe_profit_calc.bossing import BossItem
from poe_profit_calc.vendor.request import (
    PoeNinjaEndpoint,
    PoeWatchEndpoint,
    PoeEndpoint,
)
from poe_profit_calc.vendor.parse import (
    PoeNinjaCurrencyOverview,
    PoeNinjaItemOverview,
    PoeWatchJewelOverview,
    PoeNinjaItem,
    create_parser,
)


@dataclass
class PricedBossItem:
    boss_item: BossItem
    price: float
    reliable: bool
    img: str | None
    found: bool

    @staticmethod
    def not_found(item: BossItem):
        return PricedBossItem(
            boss_item=item,
            price=0,
            reliable=True,
            img=None,
            found=False,
        )

    def __hash__(self) -> int:
        return hash(self.boss_item.unique_name)


def poe_ninja_currency_matcher(
    data: PoeNinjaCurrencyOverview, items: Iterable[BossItem]
) -> dict[BossItem, PricedBossItem]:
    priced_items = {}
    name_to_currency = {}
    for currency in data.lines:
        assert currency.name not in name_to_currency, f"Duplicate currency matched: {currency.name}"
        name_to_currency[currency.name] = currency
    for item in items:
        currency_data = name_to_currency.get(item.matcher.name)
        if currency_data:
            priced_items[item] = PricedBossItem(
                boss_item=item,
                price=currency_data.chaos_value,
                reliable=True,
                img=currency_data.icon,
                found=True,
            )
        else:
            priced_items[item] = PricedBossItem.not_found(item)
    return priced_items


def poe_ninja_item_matcher(
    data: PoeNinjaItemOverview, items: Iterable[BossItem]
) -> dict[BossItem, PricedBossItem]:
    """
    Matches items from Poe Ninja to the items.

    Poe Ninja's API can return items with different variants, such as relic versions or items with 5-6 links.
    We filter out relic items and items with high links, as they do not drop from bosses immediately.
    """
    name_to_item: dict[str, PoeNinjaItem] = {}
    for item in data.lines:
        # We do not want relic items, as they do not drop from bosses immediately
        if "relic" not in item.name and "relic" in item.details_id:
            continue
        # Disregard items with high links (poeninja shows 5+ links separately)
        if item.links:
            continue

        # If we already have an item with the same name, we keep the one with the lowest chaos value
        if (
            curr_item := name_to_item.get(item.name)
        ) and curr_item.chaos_value > item.chaos_value:  # TODO swap to <
            continue
        name_to_item[item.name] = item

    priced_items = {}
    for item in items:
        item_data = name_to_item.get(item.matcher.name)
        if item_data:
            priced_items[item] = PricedBossItem(
                boss_item=item,
                price=item_data.chaos_value,
                reliable=item_data.listings >= 20,
                img=item_data.icon,
                found=True,
            )

        else:
            priced_items[item] = PricedBossItem.not_found(item)
    return priced_items


def poe_ninja_skill_gem_matcher(
    data: PoeNinjaItemOverview, items: Iterable[BossItem]
) -> dict[BossItem, PricedBossItem]:
    """
    Matches skill gems from Poe Ninja to the items.

    Poe Ninja's API can return skill gems with different variants, but we only care about the
    variant "1" which is the base variant of the skill gem, since that is the one that drops from bosses.
    """
    name_to_item = {}
    for item in data.lines:
        if item.variant != "1":
            continue
        assert item.name not in name_to_item, f"Duplicate skill gem matched: {item.name}"
        name_to_item[item.name] = item

    priced_items = {}
    for item in items:
        item_data = name_to_item.get(item.matcher.name)
        if item_data:
            priced_items[item] = PricedBossItem(
                boss_item=item,
                price=item_data.chaos_value,
                reliable=item_data.listings >= 20,
                img=item_data.icon,
                found=True,
            )
        else:
            priced_items[item] = PricedBossItem.not_found(item)
    return priced_items


def poe_watch_jewel_matcher(
    data: PoeWatchJewelOverview, items: Iterable[BossItem]
) -> dict[BossItem, PricedBossItem]:
    """
    Matches jewels from Poe Watch to the items.

    Poe Watch's API can return duplicates of jewels, each with different item levels.
    We try to find the exact match, but if we can't, we take the jewel with the lowest
    item level as to not overprice the item.
    """
    priced_items = {}
    jewels = []
    for jewel in data:
        for item in items:
            if item.matcher.name == jewel.name:
                jewels.append(jewel)
    for item in items:
        most_accurate_jewels_ilvl = None
        for jewel in jewels:
            if item.matcher.name == jewel.name:
                if jewel.item_level == item.matcher.ilvl:
                    most_accurate_jewels_ilvl = jewel
                    break
                if (
                    most_accurate_jewels_ilvl is None
                    or jewel.item_level < most_accurate_jewels_ilvl.item_level
                ):
                    most_accurate_jewels_ilvl = jewel
        if most_accurate_jewels_ilvl:
            priced_items[item] = PricedBossItem(
                boss_item=item,
                price=most_accurate_jewels_ilvl.chaos_value,
                reliable=not most_accurate_jewels_ilvl.low_confidence,
                img=most_accurate_jewels_ilvl.icon,
                found=True,
            )

        else:
            priced_items[item] = PricedBossItem.not_found(item)
    return priced_items


def get_parser_and_matcher(ep: PoeEndpoint):
    match ep:
        case PoeNinjaEndpoint.CURRENCY:
            parser = create_parser(PoeNinjaCurrencyOverview)
            matcher = poe_ninja_currency_matcher
        case PoeNinjaEndpoint.UNIQUE_ARMOUR:
            parser = create_parser(PoeNinjaItemOverview)
            matcher = poe_ninja_item_matcher
        case PoeNinjaEndpoint.UNIQUE_JEWEL:
            parser = create_parser(PoeNinjaItemOverview)
            matcher = poe_ninja_item_matcher
        case PoeNinjaEndpoint.INVITATION:
            parser = create_parser(PoeNinjaItemOverview)
            matcher = poe_ninja_item_matcher
        case PoeNinjaEndpoint.FRAGMENT:
            parser = create_parser(PoeNinjaCurrencyOverview)
            matcher = poe_ninja_currency_matcher
        case PoeNinjaEndpoint.UNIQUE_ACCESSORY:
            parser = create_parser(PoeNinjaItemOverview)
            matcher = poe_ninja_item_matcher
        case PoeNinjaEndpoint.UNIQUE_FLASK:
            parser = create_parser(PoeNinjaItemOverview)
            matcher = poe_ninja_item_matcher
        case PoeNinjaEndpoint.UNIQUE_WEAPON:
            parser = create_parser(PoeNinjaItemOverview)
            matcher = poe_ninja_item_matcher
        case PoeNinjaEndpoint.DIVINATION_CARD:
            parser = create_parser(PoeNinjaItemOverview)
            matcher = poe_ninja_item_matcher
        case PoeNinjaEndpoint.SKILL_GEM:
            parser = create_parser(PoeNinjaItemOverview)
            matcher = poe_ninja_skill_gem_matcher
        case PoeNinjaEndpoint.UNIQUE_MAP:
            parser = create_parser(PoeNinjaItemOverview)
            matcher = poe_ninja_item_matcher
        case PoeNinjaEndpoint.DELIRIUM_ORB:
            parser = create_parser(PoeNinjaItemOverview)
            matcher = poe_ninja_item_matcher
        case PoeWatchEndpoint.UNIQUE_JEWEL:
            parser = create_parser(PoeWatchJewelOverview)
            matcher = poe_watch_jewel_matcher
        case _:
            raise ValueError(f"Unknown endpoint: {ep}")
    return parser, matcher
