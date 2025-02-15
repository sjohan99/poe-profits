from enum import Enum


BASE_NINJA_URL = "https://poe.ninja/api/data/"
LEAGUE = "Settlers"
TRADE_URL = f"https://www.pathofexile.com/trade/search/{LEAGUE}"

class League(Enum):
    CURRENT = LEAGUE
    CURRENT_HC = f"Hardcore+{LEAGUE}"
    STANDARD = "Standard"
    STANDARD_HC = "Hardcore"