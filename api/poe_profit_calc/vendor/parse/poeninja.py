import msgspec


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


class PoeNinjaItemOverview(msgspec.Struct):
    lines: list[PoeNinjaItem]


class PoeNinjaCurrencyOverview(msgspec.Struct):
    lines: list[PoeNinjaCurrency]
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
            line.icon = icon


class Orb(msgspec.Struct):
    name: str
    chaos_value: float = msgspec.field(name="chaosValue")
    icon: str | None = None
    reroll_weight: int = msgspec.field(default=0)

    def __hash__(self) -> int:
        return hash(self.name)


class OrbData(msgspec.Struct):
    lines: set[Orb]


class Catalyst(msgspec.Struct):
    name: str = msgspec.field(name="currencyTypeName")
    chaos_value: float = msgspec.field(name="chaosEquivalent")
    icon: str | None = None
    details_id: str = msgspec.field(name="detailsId", default="")
    reroll_weight: int = msgspec.field(default=0)

    def __hash__(self) -> int:
        return hash(self.name)


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
