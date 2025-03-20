from poe_profit_calc.fetch.parse import (
    parse_into_type,
    PoeNinjaCurrencyOverview,
    PoeNinjaItemOverview,
    PoeWatchJewelOverview,
)
import pathlib
import pytest


class TestFetch:

    @pytest.fixture(scope="session")
    def poeninja_uniquearmour_data(self):
        file = pathlib.Path("tests/poe_ninja_data/itemoverview_uniquearmour.json")
        with open(file, "rb") as f:
            return f.read()

    @pytest.fixture(scope="session")
    def poeninja_currency_data(self):
        file = pathlib.Path("tests/poe_ninja_data/currencyoverview_currency.json")
        with open(file, "rb") as f:
            return f.read()

    @pytest.fixture(scope="session")
    def poewatch_jewel_data(self):
        file = pathlib.Path("tests/poe_watch_data/jewel.json")
        with open(file, "rb") as f:
            return f.read()

    def test_parse_poe_ninja_item_overview(self, poeninja_uniquearmour_data):
        parsed = parse_into_type(poeninja_uniquearmour_data, PoeNinjaItemOverview)
        if parsed is None:
            assert False
        assert True

    def test_parse_poe_ninja_currency_overview(self, poeninja_currency_data):
        parsed = parse_into_type(poeninja_currency_data, PoeNinjaCurrencyOverview)
        if parsed is None:
            assert False
        assert True

    def test_parse_poe_watch_jewel_overview(self, poewatch_jewel_data):
        parsed = parse_into_type(poewatch_jewel_data, PoeWatchJewelOverview)
        if parsed is None:
            assert False
        assert True
