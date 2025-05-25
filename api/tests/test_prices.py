import json
import pathlib
from poe_profit_calc.sources import Source
import pytest
from poe_profit_calc.prices import extract_prices, group_by_source
from poe_profit_calc.bossing.bossitems import *


class TestParseQuestions:
    @pytest.fixture(scope="session")
    def currency_data(self):
        file = pathlib.Path("tests/poe_ninja_data/currencyoverview_currency.json")
        with open(file, "r") as f:
            return json.loads(f.read())

    @pytest.fixture(scope="session")
    def uniquearmour_data(self):
        file = pathlib.Path("tests/poe_ninja_data/itemoverview_uniquearmour.json")
        with open(file, "r") as f:
            return json.loads(f.read())

    @pytest.fixture(scope="session")
    def uniquejewel_data(self):
        file = pathlib.Path("tests/poe_ninja_data/itemoverview_uniquejewel.json")
        with open(file, "r") as f:
            return json.loads(f.read())

    @pytest.fixture(scope="session")
    def gem_data(self):
        file = pathlib.Path("tests/poe_ninja_data/itemoverview_skillgem.json")
        with open(file, "r") as f:
            return json.loads(f.read())

    def test_process_currency(self, currency_data):
        items = {EldritchChaosOrb, EldritchExaltedOrb}
        extract_prices(currency_data, items)
        assert EldritchChaosOrb.price == 47.56
        assert EldritchExaltedOrb.price == 10

    def test_process_armour(self, uniquearmour_data):
        items = {Dawnbreaker, Dawnstrider}
        extract_prices(uniquearmour_data, items)
        assert Dawnbreaker.price == 5
        assert Dawnstrider.price == 2

    def test_process_gem(self, gem_data):
        items = {AwakenedAddedChaosDamageSupport, AwakenedEnlightenSupport}
        extract_prices(gem_data, items)
        assert AwakenedAddedChaosDamageSupport.price == 15
        assert AwakenedEnlightenSupport.price == 51476.74

    def test_group_by_source(self):
        items = {
            AwakenedAddedChaosDamageSupport,
            AwakenedEnlightenSupport,
            EldritchExaltedOrb,
            Dawnbreaker,
            EldritchChaosOrb,
            SublimeVision,
        }
        source_mapping: dict[Source, str] = {
            PoeNinjaSource.CURRENCY: "1",
            PoeNinjaSource.UNIQUE_ARMOUR: "2",
            PoeNinjaSource.SKILL_GEM: "3",
            PoeWatchSource.UNIQUE_JEWEL: "4",
        }
        grouped = group_by_source(items, source_mapping)
        assert grouped == {
            (PoeNinjaSource.CURRENCY, "1"): {EldritchExaltedOrb, EldritchChaosOrb},
            (PoeNinjaSource.UNIQUE_ARMOUR, "2"): {Dawnbreaker},
            (PoeNinjaSource.SKILL_GEM, "3"): {
                AwakenedAddedChaosDamageSupport,
                AwakenedEnlightenSupport,
            },
            (PoeWatchSource.UNIQUE_JEWEL, "4"): {SublimeVision},
        }
