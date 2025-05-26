import msgspec
import logging

VIVID_LIFEFORCE_PER_CATALYST_REROLL = 30

catalyst_weights = {
    "Abrasive Catalyst": 334,
    "Accelerating Catalyst": 82,
    "Fertile Catalyst": 83,
    "Imbued Catalyst": 281,
    "Intrinsic Catalyst": 529,
    "Noxious Catalyst": 331,
    "Prismatic Catalyst": 90,
    "Tempering Catalyst": 84,
    "Turbulent Catalyst": 330,
    "Unstable Catalyst": 84,
}


class Catalyst(msgspec.Struct):
    name: str = msgspec.field(name="currencyTypeName")
    chaos_value: float = msgspec.field(name="chaosEquivalent")
    icon: str | None = None
    details_id: str = msgspec.field(name="detailsId", default="")
    reroll_weight: int = msgspec.field(default=0)

    def __post_init__(self):
        self.reroll_weight = catalyst_weights.get(self.name, 0)

    def __hash__(self) -> int:
        return hash(self.name)


class PoeNinjaCurrencyDetails(msgspec.Struct):
    name: str
    details_id: str | None = msgspec.field(name="tradeId", default=None)
    icon: str | None = None


class CatalystData(msgspec.Struct):
    lines: set[Catalyst]
    currency_details: list[PoeNinjaCurrencyDetails] = msgspec.field(name="currencyDetails")

    def __post_init__(self):
        """
        Poe Ninja does not include the icon in the item data, but rather in the currency details.
        It seems like the detailsId for each item should map 1 to 1 with the detailsId in the currency details.
        However, on rare occasions, the detailsId is not present in the item data, in which case we try
        to match the names instead.
        """
        detail_id_to_img = {item.details_id: item.icon for item in self.currency_details}
        name_to_img = {item.name: item.icon for item in self.currency_details}
        for line in self.lines:
            icon = detail_id_to_img.get(line.details_id)
            if icon is None:
                icon = name_to_img.get(line.name)
            print(f"Setting icon for {line.name}: {icon}")
            line.icon = icon


def parse_catalysts(json_b: bytes) -> set[Catalyst]:
    try:
        parsed = msgspec.json.decode(json_b, type=CatalystData)
        catalysts = {item for item in parsed.lines if item.name in catalyst_weights}
        return catalysts
    except msgspec.DecodeError as e:
        logging.error(f"Failed to parse catalysts: {e}")
        return set()
