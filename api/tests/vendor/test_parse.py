from poe_profit_calc.vendor.parse import (
    PoeNinjaCurrencyOverview,
    PoeNinjaItemOverview,
    PoeWatchJewelOverview,
    create_parser,
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
        parsed = create_parser(PoeNinjaItemOverview)(poeninja_uniquearmour_data)
        if parsed is None:
            assert False
        assert True

    def test_parse_poe_ninja_currency_overview(self, poeninja_currency_data):
        parsed = create_parser(PoeNinjaCurrencyOverview)(poeninja_currency_data)
        if parsed is None:
            assert False
        assert True

    def test_parse_poe_watch_jewel_overview(self, poewatch_jewel_data):
        parsed = create_parser(PoeWatchJewelOverview)(poewatch_jewel_data)
        if parsed is None:
            assert False
        assert True
