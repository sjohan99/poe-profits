import asyncio
from poe_profit_calc.vendor.request.client import Client, PoeNinjaEndpoint, PoeWatchEndpoint
from poe_profit_calc.globals import League
import httpx
import pytest

poeninja_currency_url_result = "poeninja-currency"
poeninja_uniquearmour_url_result = "poeninja-uniquearmour"
poewatch_jewel_url_result = "poewatch-jewel"


def handler(request: httpx.Request):
    base_url = request.url.copy_with(query=None)
    poeninja_currency_url = "https://poe.ninja/api/data/currencyoverview"
    poeninja_uniquearmour_url = "https://poe.ninja/api/data/itemoverview"
    poewatch_jewel_url = "https://api.poe.watch/get"
    if (
        base_url == poeninja_currency_url
        and request.url.params.get("type") == "Currency"
        and request.url.params.get("league") == "Standard"
    ):
        return httpx.Response(200, content=poeninja_currency_url_result)
    elif (
        base_url == poeninja_uniquearmour_url
        and request.url.params.get("type") == "UniqueArmour"
        and request.url.params.get("league") == "Standard"
    ):
        return httpx.Response(200, content=poeninja_uniquearmour_url_result)
    elif (
        base_url == poewatch_jewel_url
        and request.url.params.get("category") == "jewel"
        and request.url.params.get("league") == "Standard"
    ):
        return httpx.Response(200, content=poewatch_jewel_url_result)
    else:
        return httpx.Response(404, content="Not Found")


class TestFetch:

    @pytest.fixture(scope="session")
    def client(self) -> Client:
        test_client = httpx.AsyncClient(
            transport=httpx.MockTransport(
                handler=handler,
            )
        )

        return Client(test_client)

    def test_existing_endpoint_returns_result(self, client: Client):
        result = asyncio.run(
            client.request_endpoints(
                [
                    PoeNinjaEndpoint.CURRENCY,
                ],
                League.STANDARD,
            )
        )
        assert result[PoeNinjaEndpoint.CURRENCY] == bytes(poeninja_currency_url_result, "utf-8")

    def test_existing_endpoint_returns_multiple_results(self, client: Client):
        results = asyncio.run(
            client.request_endpoints(
                [
                    PoeNinjaEndpoint.CURRENCY,
                    PoeNinjaEndpoint.UNIQUE_ARMOUR,
                    PoeWatchEndpoint.UNIQUE_JEWEL,
                ],
                League.STANDARD,
            )
        )

        assert results[PoeNinjaEndpoint.CURRENCY] == bytes(poeninja_currency_url_result, "utf-8")
        assert results[PoeNinjaEndpoint.UNIQUE_ARMOUR] == bytes(
            poeninja_uniquearmour_url_result, "utf-8"
        )
        assert results[PoeWatchEndpoint.UNIQUE_JEWEL] == bytes(poewatch_jewel_url_result, "utf-8")

    def test_non_existing_endpoint_returns_none(self, client: Client):
        result = asyncio.run(
            client.request_endpoints(
                [
                    PoeNinjaEndpoint.SKILL_GEM,
                ],
                League.STANDARD,
            )
        )
        assert result[PoeNinjaEndpoint.SKILL_GEM] is None

    def test_returns_results_for_valid_despite_one_request_failing(self, client: Client):
        results = asyncio.run(
            client.request_endpoints(
                [
                    PoeNinjaEndpoint.CURRENCY,
                    PoeNinjaEndpoint.UNIQUE_ARMOUR,
                    PoeWatchEndpoint.UNIQUE_JEWEL,
                    PoeNinjaEndpoint.SKILL_GEM,
                ],
                League.STANDARD,
            )
        )

        assert results[PoeNinjaEndpoint.CURRENCY] == bytes(poeninja_currency_url_result, "utf-8")
        assert results[PoeNinjaEndpoint.UNIQUE_ARMOUR] == bytes(
            poeninja_uniquearmour_url_result, "utf-8"
        )
        assert results[PoeWatchEndpoint.UNIQUE_JEWEL] == bytes(poewatch_jewel_url_result, "utf-8")
        assert results[PoeNinjaEndpoint.SKILL_GEM] is None
