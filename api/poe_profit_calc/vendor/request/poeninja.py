import httpx
from poe_profit_calc.globals import League
from .endpoints import PoeNinjaEndpoint, RequestEndpoint


class PoeNinjaClient:
    POENINJA_STASH_URL = "https://poe.ninja/poe1/api/economy/stash/current/item/overview"
    POENINJA_EXCHANGE_URL = "https://poe.ninja/poe1/api/economy/exchange/current/overview"
    LEAGUE_TO_NINJA = {
        League.STANDARD: "Standard",
        League.CURRENT_LEAGUE: "Keepers",
        League.CURRENT_LEAGUE_HC: "Keepers Hardcore",
    }
    POENINJA_ENDPOINT_MAP = {
        PoeNinjaEndpoint.CURRENCY: RequestEndpoint(
            f"{POENINJA_EXCHANGE_URL}", {"type": "Currency"}
        ),
        PoeNinjaEndpoint.UNIQUE_ARMOUR: RequestEndpoint(
            f"{POENINJA_STASH_URL}", {"type": "UniqueArmour"}
        ),
        PoeNinjaEndpoint.UNIQUE_JEWEL: RequestEndpoint(
            f"{POENINJA_STASH_URL}", {"type": "UniqueJewel"}
        ),
        PoeNinjaEndpoint.INVITATION: RequestEndpoint(
            f"{POENINJA_STASH_URL}", {"type": "Invitation"}
        ),
        PoeNinjaEndpoint.FRAGMENT: RequestEndpoint(
            f"{POENINJA_EXCHANGE_URL}", {"type": "Fragment"}
        ),
        PoeNinjaEndpoint.UNIQUE_ACCESSORY: RequestEndpoint(
            f"{POENINJA_STASH_URL}", {"type": "UniqueAccessory"}
        ),
        PoeNinjaEndpoint.UNIQUE_FLASK: RequestEndpoint(
            f"{POENINJA_STASH_URL}", {"type": "UniqueFlask"}
        ),
        PoeNinjaEndpoint.UNIQUE_WEAPON: RequestEndpoint(
            f"{POENINJA_STASH_URL}", {"type": "UniqueWeapon"}
        ),
        PoeNinjaEndpoint.DIVINATION_CARD: RequestEndpoint(
            f"{POENINJA_EXCHANGE_URL}", {"type": "DivinationCard"}
        ),
        PoeNinjaEndpoint.SKILL_GEM: RequestEndpoint(f"{POENINJA_STASH_URL}", {"type": "SkillGem"}),
        PoeNinjaEndpoint.UNIQUE_MAP: RequestEndpoint(
            f"{POENINJA_STASH_URL}", {"type": "UniqueMap"}
        ),
        PoeNinjaEndpoint.DELIRIUM_ORB: RequestEndpoint(
            f"{POENINJA_EXCHANGE_URL}", {"type": "DeliriumOrb"}
        ),
        PoeNinjaEndpoint.ALLFLAME_EMBERS: RequestEndpoint(
            f"{POENINJA_EXCHANGE_URL}", {"type": "AllflameEmber"}
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
        league_id = self.LEAGUE_TO_NINJA[league]
        return self.client.get(
            endpoint.url,
            params=endpoint.params | {"league": league_id} | extra_params,
            headers=headers,
        )
