import msgspec

POE_CDN_BASE_URL = "https://web.poecdn.com"


class PoeNinjaItem(msgspec.Struct):
    name: str
    details_id: str = msgspec.field(name="detailsId")
    chaos_value: float = msgspec.field(name="chaosValue", default=-1)
    listings: int = msgspec.field(name="listingCount", default=0)
    icon: str | None = None
    links: int | None = None
    variant: str | None = None


class PoeNinjaCurrency(msgspec.Struct):
    id: str
    chaos_value: float = msgspec.field(name="primaryValue")
    name: str | None = None
    icon: str | None = None


class PoeNinjaCurrencyDetails(msgspec.Struct):
    name: str
    id: str
    icon: str | None = msgspec.field(name="image", default=None)


class PoeNinjaItemOverview(msgspec.Struct):
    lines: list[PoeNinjaItem]


class PoeNinjaCurrencyOverview(msgspec.Struct):
    lines: list[PoeNinjaCurrency]
    currency_details: list[PoeNinjaCurrencyDetails] = msgspec.field(name="items")

    def __post_init__(self):
        id_to_details = {item.id: item for item in self.currency_details}
        for line in self.lines:
            details = id_to_details.get(line.id)
            if details:
                line.name = details.name
                line.icon = f"{POE_CDN_BASE_URL}{details.icon}"


class Orb(msgspec.Struct):
    id: str
    chaos_value: float = msgspec.field(name="primaryValue")
    name: str = "Unknown"
    icon: str | None = None
    reroll_weight: int = msgspec.field(default=0)

    def __hash__(self) -> int:
        return hash(self.id)


class OrbData(msgspec.Struct):
    lines: set[Orb]
    currency_details: list[PoeNinjaCurrencyDetails] = msgspec.field(name="items")

    def __post_init__(self):
        id_to_details = {item.id: item for item in self.currency_details}
        for line in self.lines:
            details = id_to_details.get(line.id)
            if details:
                line.name = details.name
                line.icon = f"{POE_CDN_BASE_URL}{details.icon}"


class Catalyst(msgspec.Struct):
    id: str
    chaos_value: float = msgspec.field(name="primaryValue")
    name: str = "Unknown"
    icon: str | None = None
    reroll_weight: int = msgspec.field(default=0)

    def __hash__(self) -> int:
        return hash(self.id)


class CatalystData(msgspec.Struct):
    lines: set[Catalyst]
    currency_details: list[PoeNinjaCurrencyDetails] = msgspec.field(name="items")

    def __post_init__(self):
        id_to_details = {item.id: item for item in self.currency_details}
        for line in self.lines:
            details = id_to_details.get(line.id)
            if details:
                line.name = details.name
                line.icon = f"{POE_CDN_BASE_URL}{details.icon}"
