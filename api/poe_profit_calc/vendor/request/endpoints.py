from dataclasses import dataclass
from enum import Enum


class PoeNinjaEndpoint(Enum):
    CURRENCY = "Currency"
    FRAGMENT = "Fragment"
    UNIQUE_ARMOUR = "UniqueArmour"
    UNIQUE_JEWEL = "UniqueJewel"
    INVITATION = "Invitation"
    UNIQUE_ACCESSORY = "UniqueAccessory"
    UNIQUE_FLASK = "UniqueFlask"
    UNIQUE_WEAPON = "UniqueWeapon"
    DIVINATION_CARD = "DivinationCard"
    SKILL_GEM = "SkillGem"
    UNIQUE_MAP = "UniqueMap"
    DELIRIUM_ORB = "DeliriumOrb"
    ALLFLAME_EMBERS = "AllflameEmbers"


class PoeWatchEndpoint(Enum):
    UNIQUE_JEWEL = "jewel"
    FRAGMENT = "fragment"
    CURRENCY = "currency"


PoeEndpoint = PoeNinjaEndpoint | PoeWatchEndpoint


@dataclass
class RequestEndpoint:
    url: str
    params: dict[str, str]
