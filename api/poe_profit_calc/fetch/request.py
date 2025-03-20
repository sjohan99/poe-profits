import asyncio
import logging
import hishel
import httpx
from types import CoroutineType
from typing import Tuple
from dataclasses import dataclass
from enum import Enum
from poe_profit_calc.globals import League


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


class PoeWatchEndpoint(Enum):
    UNIQUE_JEWEL = "jewel"


PoeEndpoint = PoeNinjaEndpoint | PoeWatchEndpoint


@dataclass
class RequestEndpoint:
    url: str
    params: dict[str, str]


class PoeNinjaClient:
    POENINJA_BASE_URL = "https://poe.ninja/api/data"
    LEAGUE_TO_NINJA = {
        League.SETTLERS: "Settlers",
        League.SETTLERS_HC: "Hardcore+Settlers",
        League.STANDARD: "Standard",
        League.STANDARD_HC: "Hardcore",
        League.PHRECIA: "Phrecia",
        League.PHRECIA_HC: "Hardcore+Phrecia",
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
        self.base_url = "https://poe.ninja/api/data"

    def create_request(self, poeninja_endpoint: PoeNinjaEndpoint, league: League, params=None):
        extra_params = params or {}
        endpoint = self.POENINJA_ENDPOINT_MAP[poeninja_endpoint]
        return self.client.get(
            endpoint.url, params=endpoint.params | {"league": league.value} | extra_params
        )


class PoeWatchClient:
    POEWATCH_BASE_URL = "https://api.poe.watch"
    LEAGUE_TO_POE_WATCH = {
        League.SETTLERS: "Settlers",
        League.SETTLERS_HC: "Hardcore+Settlers",
        League.STANDARD: "Standard",
        League.STANDARD_HC: "Hardcore",
        League.PHRECIA: "Phrecia",
        League.PHRECIA_HC: "Hardcore+Phrecia",
    }
    POEWATCH_ENDPOINT_MAP = {
        PoeWatchEndpoint.UNIQUE_JEWEL: RequestEndpoint(
            f"{POEWATCH_BASE_URL}/get", {"category": "jewel"}
        )
    }

    def __init__(self, client: httpx.AsyncClient):
        self.client = client
        self.base_url = self.POEWATCH_BASE_URL

    def create_request(self, poewatch_endpoint: PoeWatchEndpoint, league: League, params=None):
        extra_params = params or {}
        endpoint = self.POEWATCH_ENDPOINT_MAP[poewatch_endpoint]
        return self.client.get(
            endpoint.url, params=endpoint.params | {"league": league.value} | extra_params
        )


class Client:
    def __init__(self, client: httpx.AsyncClient | hishel.AsyncCacheClient | None = None):
        if client is None:
            controller = hishel.Controller(
                cacheable_methods=["GET"],
                cacheable_status_codes=[200],
                allow_stale=True,
            )
            storage = hishel.InMemoryStorage(capacity=128, ttl=1800)
            client = hishel.AsyncCacheClient(controller=controller, storage=storage)

        self.client = client
        self.poeninja = PoeNinjaClient(self.client)
        self.poewatch = PoeWatchClient(self.client)

    def request_endpoints(
        self, league: League, endpoints: list[PoeEndpoint]
    ) -> dict[PoeEndpoint, bytes | None]:
        requests: list[Tuple[PoeEndpoint, CoroutineType]] = []
        for endpoint in endpoints:
            if isinstance(endpoint, PoeWatchEndpoint):
                requests.append((endpoint, self.poewatch.create_request(endpoint, league)))
            elif isinstance(endpoint, PoeNinjaEndpoint):
                requests.append((endpoint, self.poeninja.create_request(endpoint, league)))

        return asyncio.run(self._make_requests(requests))

    async def _make_request(self, request) -> httpx.Response | None:
        try:
            response: httpx.Response = await request
            response.raise_for_status()
        except httpx.HTTPError as e:
            logging.error(f"Failed to fetch data from {e.request.url} with message: {str(e)}")
            return None
        return response

    async def _make_requests(
        self, requests: list[Tuple[PoeEndpoint, CoroutineType]]
    ) -> dict[PoeEndpoint, bytes | None]:
        endpoints, _requests = zip(*requests)
        responses: list[httpx.Response | None] = await asyncio.gather(
            *[self._make_request(request) for request in _requests]
        )
        response_data = [response.content if response else None for response in responses]
        return dict(zip(endpoints, response_data))
