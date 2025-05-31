import httpx
from poe_profit_calc.globals import League
from .endpoints import PoeNinjaEndpoint, RequestEndpoint


class PoeNinjaClient:
    POENINJA_BASE_URL = "https://poe.ninja/api/data"
    LEAGUE_TO_NINJA = {
        League.STANDARD: "Standard",
    }
    POENINJA_ENDPOINT_MAP = {
        PoeNinjaEndpoint.CURRENCY: RequestEndpoint(
            f"{POENINJA_BASE_URL}/currencyoverview", {"type": "Currency"}
        ),
        PoeNinjaEndpoint.UNIQUE_ARMOUR: RequestEndpoint(
            f"{POENINJA_BASE_URL}/itemoverview", {"type": "UniqueArmour"}
        ),
        PoeNinjaEndpoint.UNIQUE_JEWEL: RequestEndpoint(
            f"{POENINJA_BASE_URL}/itemoverview", {"type": "UniqueJewel"}
        ),
        PoeNinjaEndpoint.INVITATION: RequestEndpoint(
            f"{POENINJA_BASE_URL}/itemoverview", {"type": "Invitation"}
        ),
        PoeNinjaEndpoint.FRAGMENT: RequestEndpoint(
            f"{POENINJA_BASE_URL}/currencyoverview", {"type": "Fragment"}
        ),
        PoeNinjaEndpoint.UNIQUE_ACCESSORY: RequestEndpoint(
            f"{POENINJA_BASE_URL}/itemoverview", {"type": "UniqueAccessory"}
        ),
        PoeNinjaEndpoint.UNIQUE_FLASK: RequestEndpoint(
            f"{POENINJA_BASE_URL}/itemoverview", {"type": "UniqueFlask"}
        ),
        PoeNinjaEndpoint.UNIQUE_WEAPON: RequestEndpoint(
            f"{POENINJA_BASE_URL}/itemoverview", {"type": "UniqueWeapon"}
        ),
        PoeNinjaEndpoint.DIVINATION_CARD: RequestEndpoint(
            f"{POENINJA_BASE_URL}/itemoverview", {"type": "DivinationCard"}
        ),
        PoeNinjaEndpoint.SKILL_GEM: RequestEndpoint(
            f"{POENINJA_BASE_URL}/itemoverview", {"type": "SkillGem"}
        ),
        PoeNinjaEndpoint.UNIQUE_MAP: RequestEndpoint(
            f"{POENINJA_BASE_URL}/itemoverview", {"type": "UniqueMap"}
        ),
        PoeNinjaEndpoint.DELIRIUM_ORB: RequestEndpoint(
            f"{POENINJA_BASE_URL}/itemoverview", {"type": "DeliriumOrb"}
        ),
    }

    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    def create_request_coroutine(
        self, poeninja_endpoint: PoeNinjaEndpoint, league: League, params=None, headers=None
    ):
        extra_params = params or {}
        headers = headers or {}
        endpoint = self.POENINJA_ENDPOINT_MAP[poeninja_endpoint]
        return self.client.get(
            endpoint.url,
            params=endpoint.params | {"league": league.value} | extra_params,
            headers=headers,
        )
