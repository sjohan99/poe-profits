import httpx
from poe_profit_calc.globals import League
from .endpoints import PoeWatchEndpoint, RequestEndpoint


class PoeWatchClient:
    POEWATCH_BASE_URL = "https://api.poe.watch"
    LEAGUE_TO_POE_WATCH = {
        League.STANDARD: "Standard",
    }
    POEWATCH_ENDPOINT_MAP = {
        PoeWatchEndpoint.UNIQUE_JEWEL: RequestEndpoint(
            f"{POEWATCH_BASE_URL}/get", {"category": "jewel"}
        )
    }

    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    def create_request_coroutine(
        self, poewatch_endpoint: PoeWatchEndpoint, league: League, params=None, headers=None
    ):
        extra_params = params or {}
        headers = headers or {}
        endpoint = self.POEWATCH_ENDPOINT_MAP[poewatch_endpoint]
        return self.client.get(
            endpoint.url,
            params=endpoint.params | {"league": league.value} | extra_params,
            headers=headers,
        )
