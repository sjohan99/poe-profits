import asyncio
import logging
import hishel
import httpx
from types import CoroutineType
from typing import Iterable, Tuple
from poe_profit_calc.globals import League
from .endpoints import PoeEndpoint, PoeNinjaEndpoint, PoeWatchEndpoint
from .poeninja import PoeNinjaClient
from .poewatch import PoeWatchClient


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
        num_cached = sum(
            1
            for response in responses
            if response is not None and response.extensions.get("from_cache") is True
        )
        logging.getLogger("hishel.controller").info(
            f"Fetched {num_cached} out of {len(endpoints)} endpoints from cache."
        )
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

    def __init__(self, path_prefix: str = ""):
        super().__init__(client=None)
        self._path_prefix = path_prefix

    async def request_endpoints(
        self,
        endpoints: Iterable[PoeEndpoint],
        league: League,
    ) -> dict[PoeEndpoint, bytes | None]:
        result = {}
        for endpoint in endpoints:
            path = self.file_paths.get(endpoint)
            if path:
                path = f"{self._path_prefix}/{path}" if self._path_prefix else path
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
            path = f"{self._path_prefix}/{path}" if self._path_prefix else path
            try:
                with open(path, "rb") as f:
                    return f.read()
            except Exception as e:
                logging.error(f"Failed to read file {path}: {e}")
                return None
        return None
