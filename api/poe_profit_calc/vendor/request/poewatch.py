import httpx
from poe_profit_calc.globals import League
from .endpoints import PoeWatchEndpoint, RequestEndpoint


class PoeWatchClient:
    POEWATCH_BASE_URL = "https://api.poe.watch"
    LEAGUE_TO_POE_WATCH = {
        League.STANDARD: "Standard",
        League.CURRENT_LEAGUE: "Keepers",
        League.CURRENT_LEAGUE_HC: "Hardcore Keepers",
    }
    POEWATCH_ENDPOINT_MAP = {
        PoeWatchEndpoint.UNIQUE_JEWEL: RequestEndpoint(
            f"{POEWATCH_BASE_URL}/get", {"category": "jewel"}
        ),
        PoeWatchEndpoint.FRAGMENT: RequestEndpoint(
            f"{POEWATCH_BASE_URL}/get", {"category": "fragment"}
        ),
        PoeWatchEndpoint.CURRENCY: RequestEndpoint(
            f"{POEWATCH_BASE_URL}/get", {"category": "currency"}
        ),
    }

    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    def create_request_coroutine(
        self, poewatch_endpoint: PoeWatchEndpoint, league: League, params=None, headers=None
    ):
        extra_params = params or {}
        headers = headers or {}
        endpoint = self.POEWATCH_ENDPOINT_MAP[poewatch_endpoint]
        league_id = self.LEAGUE_TO_POE_WATCH[league]
        return self.client.get(
            endpoint.url,
            params=endpoint.params | {"league": league_id} | extra_params,
            headers=headers,
        )
