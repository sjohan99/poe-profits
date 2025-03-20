import asyncio
import logging
import hishel
import httpx
from types import CoroutineType
from typing import Iterable, Tuple
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

    def create_request_coroutine(
        self, poeninja_endpoint: PoeNinjaEndpoint, league: League, params=None
    ):
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

    def create_request_coroutine(
        self, poewatch_endpoint: PoeWatchEndpoint, league: League, params=None
    ):
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
            storage = hishel.AsyncInMemoryStorage(capacity=128, ttl=1800)
            client = hishel.AsyncCacheClient(controller=controller, storage=storage)

        self._client = client
        self._poeninja = PoeNinjaClient(self._client)
        self._poewatch = PoeWatchClient(self._client)

    async def request_endpoints(
        self, endpoints: Iterable[PoeEndpoint], league: League
    ) -> dict[PoeEndpoint, bytes | None]:
        requests: list[Tuple[PoeEndpoint, CoroutineType]] = []
        for endpoint in endpoints:
            match endpoint:
                case PoeWatchEndpoint():
                    requests.append(
                        (endpoint, self._poewatch.create_request_coroutine(endpoint, league))
                    )
                case PoeNinjaEndpoint():
                    requests.append(
                        (endpoint, self._poeninja.create_request_coroutine(endpoint, league))
                    )

        return await self._make_requests(requests)

    async def request_endpoint(
        self,
        endpoint: PoeEndpoint,
        league: League,
    ) -> bytes | None:
        requests: list[Tuple[PoeEndpoint, CoroutineType]] = []
        match endpoint:
            case PoeWatchEndpoint():
                requests.append(
                    (endpoint, self._poewatch.create_request_coroutine(endpoint, league))
                )
            case PoeNinjaEndpoint():
                requests.append(
                    (endpoint, self._poeninja.create_request_coroutine(endpoint, league))
                )

        res = await self._make_requests(requests)
        return res.get(endpoint)

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


class LocalClient(Client):
    """
    A local client that does not use any external APIs.
    It is used for testing purposes only.
    """

    file_paths = {
        PoeNinjaEndpoint.CURRENCY: "static/currencyoverview_currency.json",
        PoeNinjaEndpoint.UNIQUE_ARMOUR: "static/itemoverview_uniquearmour.json",
        PoeNinjaEndpoint.UNIQUE_JEWEL: "static/itemoverview_uniquejewel.json",
        PoeNinjaEndpoint.INVITATION: "static/itemoverview_invitation.json",
        PoeNinjaEndpoint.FRAGMENT: "static/currencyoverview_fragment.json",
        PoeNinjaEndpoint.UNIQUE_ACCESSORY: "static/itemoverview_uniqueaccessory.json",
        PoeNinjaEndpoint.UNIQUE_FLASK: "static/itemoverview_uniqueflask.json",
        PoeNinjaEndpoint.UNIQUE_WEAPON: "static/itemoverview_uniqueweapon.json",
        PoeNinjaEndpoint.DIVINATION_CARD: "static/itemoverview_divinationcard.json",
        PoeNinjaEndpoint.SKILL_GEM: "static/itemoverview_skillgem.json",
        PoeNinjaEndpoint.UNIQUE_MAP: "static/itemoverview_uniquemap.json",
        PoeNinjaEndpoint.DELIRIUM_ORB: "static/itemoverview_deliriumorb.json",
        PoeWatchEndpoint.UNIQUE_JEWEL: "static/poewatch/jewel.json",
    }

    def __init__(self):
        super().__init__(client=None)

    async def request_endpoints(
        self,
        endpoints: Iterable[PoeEndpoint],
        league: League,
    ) -> dict[PoeEndpoint, bytes | None]:
        result = {}
        for endpoint in endpoints:
            path = self.file_paths.get(endpoint)
            if path:
                try:
                    with open(path, "rb") as f:
                        result[endpoint] = f.read()
                except Exception as e:
                    logging.error(f"Failed to read file {path}: {e}")
                    result[endpoint] = None
            else:
                result[endpoint] = None
        return result

    async def request_endpoint(
        self,
        endpoint: PoeEndpoint,
        league: League,
    ) -> bytes | None:
        logging.warning(f"LocalClient is used, no actual request will be made for {endpoint.name}.")
        path = self.file_paths.get(endpoint)
        if path:
            try:
                with open(path, "rb") as f:
                    return f.read()
            except Exception as e:
                logging.error(f"Failed to read file {path}: {e}")
                return None
        return None
