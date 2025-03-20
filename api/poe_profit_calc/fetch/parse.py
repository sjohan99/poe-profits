import msgspec
import logging
from typing import Type, TypeVar
from typing import Callable


class PoeNinjaItem(msgspec.Struct):
    name: str
    details_id: str = msgspec.field(name="detailsId")
    chaos_value: float = msgspec.field(name="chaosValue", default=-1)
    listings: int = msgspec.field(name="listingCount", default=0)
    icon: str | None = None
    links: int | None = None
    variant: str | None = None


class Receive(msgspec.Struct):
    value: float


class PoeNinjaCurrency(msgspec.Struct):
    name: str = msgspec.field(name="currencyTypeName")
    details_id: str = msgspec.field(name="detailsId")
    chaos_value: float = msgspec.field(name="chaosEquivalent")
    receive: Receive
    icon: str | None = None


class PoeNinjaCurrencyDetails(msgspec.Struct):
    name: str
    details_id: str | None = msgspec.field(name="tradeId", default=None)
    icon: str | None = None


class PoeWatchJewel(msgspec.Struct):
    name: str
    chaos_value: float = msgspec.field(name="mean", default=-1)
    icon: str | None = None
    low_confidence: bool = msgspec.field(name="lowConfidence", default=True)
    item_level: int = msgspec.field(name="itemLevel", default=-1)


class PoeNinjaItemOverview(msgspec.Struct):
    lines: list[PoeNinjaItem]


class PoeNinjaCurrencyOverview(msgspec.Struct):
    lines: list[PoeNinjaCurrency]
    currency_details: list[PoeNinjaCurrencyDetails] = msgspec.field(name="currencyDetails")

    def __post_init__(self):
        detail_id_to_img = {item.details_id: item.icon for item in self.currency_details}
        for line in self.lines:
            line.icon = detail_id_to_img.get(line.details_id)


# poewatch returns a json array as the root, rather than an object
PoeWatchJewelOverview = list[PoeWatchJewel]

JsonDataStruct = TypeVar("JsonDataStruct", bound=msgspec.Struct | PoeWatchJewelOverview)


def parse_into_type(json_bytes: bytes, type_: Type[JsonDataStruct]) -> JsonDataStruct | None:
    try:
        parsed = msgspec.json.decode(json_bytes, type=type_)
        return parsed
    except msgspec.DecodeError as e:
        logging.error(f"Msgspec failed to decode bytes into type: {type_}. Error message: {e}")
        return None


def create_parser(type_: Type[JsonDataStruct]) -> Callable[[bytes], JsonDataStruct | None]:
    def parse_fn(json_bytes: bytes) -> JsonDataStruct | None:
        return parse_into_type(json_bytes, type_)

    return parse_fn
