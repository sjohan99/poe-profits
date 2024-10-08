from dataclasses import dataclass, field
from poe_profit_calc.sources import SOURCE_TO_FIELDS, PoeNinjaSource
from poe_profit_calc.utils import nested_get
import logging


@dataclass
class MatchResult:
    price: float
    img: str


@dataclass
class PoeNinjaMatcher:
    """
    Attributes:
        source: Source for the item, indicates in which data-set the item is found in.
        name: Name of the item to match.
        match_fields: Key-value pairs to match against the item. Must match all key-value pairs.
        exclude_fields: Key-value pairs to exclude from the item.
                        Must not match any key-value pairs.
                        If the value is an empty set, the key must not exist in the item.
        name_field_key: Key to match the name of the item against.
        price_field_keys: A list of keys to navigate through the item dictionary to get the price.
    """

    source: PoeNinjaSource
    name: str
    match_fields: dict = field(default_factory=dict)
    exclude_fields: dict[str, set] = field(default_factory=dict)
    name_field_key: str = ""
    price_field_keys: list[str] = field(default_factory=list)

    def try_match(self, item: dict) -> MatchResult | None:
        if item.get(self.name_field_key) != self.name:
            return None
        if "relic" not in self.name and "relic" in item.get("detailsId", ""):
            return None
        for key, value in self.match_fields.items():
            if item.get(key) != value:
                return None
        for key, exclude_values in self.exclude_fields.items():
            if key in item and not exclude_values:
                return None
            field_value = item.get(key)
            for exclude_value in exclude_values:
                if field_value == exclude_value:
                    return None
        try:
            price = nested_get(item, self.price_field_keys)
            if not isinstance(price, (float, int)):
                logging.warning(
                    f"Price for {self.name} is not a number: {price}. Defaulting to -1."
                )
                price = -1
        except KeyError:
            price = -1
        return MatchResult(price, item.get("icon", ""))

    def try_match_currency_details(self, item: dict) -> str | None:
        if item.get("name") == self.name:
            return item.get("icon", "")
        return None

    def __post_init__(self):
        if not self.name_field_key:
            self.name_field_key = SOURCE_TO_FIELDS[self.source]["name"]

        if not self.price_field_keys:
            self.price_field_keys = [SOURCE_TO_FIELDS[self.source]["price"]]

        if self.source == PoeNinjaSource.SKILL_GEM:
            self.match_fields["variant"] = "1"

        if (
            self.source == PoeNinjaSource.UNIQUE_ARMOUR
            or self.source == PoeNinjaSource.UNIQUE_WEAPON
        ):
            self.exclude_fields["links"] = set()


@dataclass
class Item:
    name: str
    unique_name: str
    droprate: float
    matcher: PoeNinjaMatcher
    price: float = 0
    img: str | None = None
    reliable: bool = True
    trade_link: str | None = None
    metadata: dict = field(default_factory=dict)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Item):
            return self.unique_name == value.unique_name
        return False

    def __hash__(self) -> int:
        return hash(self.unique_name)

    def match(self, item: dict) -> bool:
        res = self.matcher.try_match(item)
        if res is not None:
            self.img = res.img
            self.price = res.price
            return True
        return False

    def match_currency_details(self, item: dict) -> bool:
        if (img := self.matcher.try_match_currency_details(item)) is not None:
            self.img = img
            return True
        return False
