from poe_profit_calc.items import Item, PoeNinjaMatcher
from poe_profit_calc.sources import PoeNinjaSource


PrimalCrystallisedLifeforce = Item(
    "Primal Crystallised Lifeforce",
    "PrimalCrystallisedLifeforce",
    0,
    PoeNinjaMatcher(
        PoeNinjaSource.CURRENCY,
        "Primal Crystallised Lifeforce",
        price_field_keys=["receive", "value"],
    ),
)

VividCrystallisedLifeforce = Item(
    "Vivid Crystallised Lifeforce",
    "VividCrystallisedLifeforce",
    0,
    PoeNinjaMatcher(
        PoeNinjaSource.CURRENCY,
        "Vivid Crystallised Lifeforce",
        price_field_keys=["receive", "value"],
    ),
)

WildCrystallisedLifeforce = Item(
    "Wild Crystallised Lifeforce",
    "WildCrystallisedLifeforce",
    0,
    PoeNinjaMatcher(
        PoeNinjaSource.CURRENCY,
        "Wild Crystallised Lifeforce",
        price_field_keys=["receive", "value"],
    ),
)
