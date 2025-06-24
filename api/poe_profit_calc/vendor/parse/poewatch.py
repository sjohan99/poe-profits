import msgspec


class PoeWatchJewel(msgspec.Struct):
    name: str
    chaos_value: float = msgspec.field(name="mean", default=-1)
    icon: str | None = None
    low_confidence: bool = msgspec.field(name="lowConfidence", default=True)
    item_level: int = msgspec.field(name="itemLevel", default=-1)


# poewatch returns a json array as the root, rather than an object
PoeWatchJewelOverview = list[PoeWatchJewel]


class PoeWatchFragment(msgspec.Struct):
    name: str
    chaos_value: float = msgspec.field(name="mean", default=-1)
    icon: str | None = None
    low_confidence: bool = msgspec.field(name="lowConfidence", default=True)


PoeWatchFragmentOverview = list[PoeWatchFragment]
