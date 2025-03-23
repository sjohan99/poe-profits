from enum import Enum
from poe_profit_calc.globals import BASE_NINJA_URL, BASE_POE_WATCH_URL, League


class PoeNinjaSource(Enum):
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


class PoeWatchSource(Enum):
    UNIQUE_JEWEL = "jewel"


Source = PoeNinjaSource | PoeWatchSource

LEAGUE_TO_NINJA = {
    League.SETTLERS: "Settlers",
    League.SETTLERS_HC: "Hardcore+Settlers",
    League.STANDARD: "Standard",
    League.PHRECIA: "Phrecia",
    League.PHRECIA_HC: "Hardcore+Phrecia",
}

LEAGUE_TO_POE_WATCH = {
    League.SETTLERS: "Settlers",
    League.SETTLERS_HC: "Hardcore+Settlers",
    League.STANDARD: "Standard",
    League.PHRECIA: "Phrecia",
    League.PHRECIA_HC: "Hardcore+Phrecia",
}

SOURCE_TO_FIELDS = {
    PoeNinjaSource.CURRENCY: {"name": "currencyTypeName", "price": "chaosEquivalent"},
    PoeNinjaSource.FRAGMENT: {"name": "currencyTypeName", "price": "chaosEquivalent"},
    PoeNinjaSource.UNIQUE_ARMOUR: {"name": "name", "price": "chaosValue"},
    PoeNinjaSource.UNIQUE_JEWEL: {"name": "name", "price": "chaosValue"},
    PoeNinjaSource.INVITATION: {"name": "name", "price": "chaosValue"},
    PoeNinjaSource.UNIQUE_ACCESSORY: {"name": "name", "price": "chaosValue"},
    PoeNinjaSource.UNIQUE_FLASK: {"name": "name", "price": "chaosValue"},
    PoeNinjaSource.UNIQUE_WEAPON: {"name": "name", "price": "chaosValue"},
    PoeNinjaSource.DIVINATION_CARD: {"name": "name", "price": "chaosValue"},
    PoeNinjaSource.SKILL_GEM: {"name": "name", "price": "chaosValue"},
    PoeNinjaSource.UNIQUE_MAP: {"name": "name", "price": "chaosValue"},
    PoeNinjaSource.DELIRIUM_ORB: {"name": "name", "price": "chaosValue"},
}


def make_endpoint_mapping(league: League):
    ninja_league = LEAGUE_TO_NINJA[league]
    poe_watch_league = LEAGUE_TO_POE_WATCH[league]
    return {
        PoeNinjaSource.CURRENCY: f"{BASE_NINJA_URL}currencyoverview?league={ninja_league}&type=Currency",
        PoeNinjaSource.UNIQUE_ARMOUR: f"{BASE_NINJA_URL}itemoverview?league={ninja_league}&type=UniqueArmour",
        PoeNinjaSource.UNIQUE_JEWEL: f"{BASE_NINJA_URL}itemoverview?league={ninja_league}&type=UniqueJewel",
        PoeNinjaSource.INVITATION: f"{BASE_NINJA_URL}itemoverview?league={ninja_league}&type=Invitation",
        PoeNinjaSource.FRAGMENT: f"{BASE_NINJA_URL}currencyoverview?league={ninja_league}&type=Fragment",
        PoeNinjaSource.UNIQUE_ACCESSORY: f"{BASE_NINJA_URL}itemoverview?league={ninja_league}&type=UniqueAccessory",
        PoeNinjaSource.UNIQUE_FLASK: f"{BASE_NINJA_URL}itemoverview?league={ninja_league}&type=UniqueFlask",
        PoeNinjaSource.UNIQUE_WEAPON: f"{BASE_NINJA_URL}itemoverview?league={ninja_league}&type=UniqueWeapon",
        PoeNinjaSource.DIVINATION_CARD: f"{BASE_NINJA_URL}itemoverview?league={ninja_league}&type=DivinationCard",
        PoeNinjaSource.SKILL_GEM: f"{BASE_NINJA_URL}itemoverview?league={ninja_league}&type=SkillGem",
        PoeNinjaSource.UNIQUE_MAP: f"{BASE_NINJA_URL}itemoverview?league={ninja_league}&type=UniqueMap",
        PoeNinjaSource.DELIRIUM_ORB: f"{BASE_NINJA_URL}itemoverview?league={ninja_league}&type=DeliriumOrb",
        PoeWatchSource.UNIQUE_JEWEL: f"{BASE_POE_WATCH_URL}get?category=jewel&league={poe_watch_league}",
    }


FILE_PATH_MAPPING = {
    PoeNinjaSource.CURRENCY: "static/currencyoverview_currency.json",
    PoeNinjaSource.UNIQUE_ARMOUR: "static/itemoverview_uniquearmour.json",
    PoeNinjaSource.UNIQUE_JEWEL: "static/itemoverview_uniquejewel.json",
    PoeNinjaSource.INVITATION: "static/itemoverview_invitation.json",
    PoeNinjaSource.FRAGMENT: "static/currencyoverview_fragment.json",
    PoeNinjaSource.UNIQUE_ACCESSORY: "static/itemoverview_uniqueaccessory.json",
    PoeNinjaSource.UNIQUE_FLASK: "static/itemoverview_uniqueflask.json",
    PoeNinjaSource.UNIQUE_WEAPON: "static/itemoverview_uniqueweapon.json",
    PoeNinjaSource.DIVINATION_CARD: "static/itemoverview_divinationcard.json",
    PoeNinjaSource.SKILL_GEM: "static/itemoverview_skillgem.json",
    PoeNinjaSource.UNIQUE_MAP: "static/itemoverview_uniquemap.json",
    PoeNinjaSource.DELIRIUM_ORB: "static/itemoverview_deliriumorb.json",
    PoeWatchSource.UNIQUE_JEWEL: "static/poewatch/jewel.json",
}
