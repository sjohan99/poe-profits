from enum import Enum


BASE_NINJA_URL = "https://poe.ninja/api/data/"
BASE_POE_WATCH_URL = "https://api.poe.watch/"
LEAGUE = "Settlers"


class League(Enum):
    PHRECIA = "Phrecia"
    PHRECIA_HC = "Phrecia-Hardcore"
    SETTLERS = "Settlers"
    SETTLERS_HC = f"Settlers-Hardcore"
    STANDARD = "Standard"
    STANDARD_HC = "Hardcore"


TRADE_BASE_URL = f"https://www.pathofexile.com/trade/search/{LEAGUE}"
TRADE_URLS = {
    League.SETTLERS: f"https://www.pathofexile.com/trade/search/{'Settlers'}",
    League.SETTLERS_HC: f"https://www.pathofexile.com/trade/search/{'Hardcore%20Settlers'}",
    League.STANDARD: f"https://www.pathofexile.com/trade/search/{'Standard'}",
    League.STANDARD_HC: f"https://www.pathofexile.com/trade/search/{'Hardcore'}",
    League.PHRECIA: f"https://www.pathofexile.com/trade/search/{'Phrecia'}",
    League.PHRECIA_HC: f"https://www.pathofexile.com/trade/search/{'Hardcore%20Phrecia'}",
}
