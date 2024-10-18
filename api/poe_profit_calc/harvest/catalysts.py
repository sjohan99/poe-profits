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
    reroll_weight: int = msgspec.field(default=0)

    def __post_init__(self):
        self.reroll_weight = catalyst_weights.get(self.name, 0)

    def __hash__(self) -> int:
        return hash(self.name)


class CatalystMetadata(msgspec.Struct):
    name: str
    icon: str | None = None

    def __hash__(self) -> int:
        return hash(self.name)


class CatalystData(msgspec.Struct):
    lines: set[Catalyst]


class CMD(msgspec.Struct):
    currencyDetails: set[CatalystMetadata]


def parse_catalysts(json_b: bytes) -> set[Catalyst]:
    try:
        parsed = msgspec.json.decode(json_b, type=CatalystData)
        catalysts = {item for item in parsed.lines if item.name in catalyst_weights}
    except msgspec.DecodeError as e:
        logging.error(f"Failed to parse catalysts: {e}")
        return set()

    try:
        metadata = msgspec.json.decode(json_b, type=CMD)
        for metadata in metadata.currencyDetails:
            for catalyst in catalysts:
                if catalyst.name == metadata.name:
                    catalyst.icon = metadata.icon
        return catalysts
    except msgspec.DecodeError as e:
        logging.error(f"Failed to parse catalyst metadata: {e}")
        return catalysts
