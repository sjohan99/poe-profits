import pathlib
from poe_profit_calc.harvest.orbs import Orb
import pytest
from poe_profit_calc.harvest.orbs import parse_orbs


class TestParseQuestions:
    @pytest.fixture(scope="session")
    def orb_data(self) -> bytes:
        file = pathlib.Path(pathlib.Path(__file__).parent, "data/itemoverview_deliriumorb.json")
        with open(file, "rb") as f:
            return f.read()

    @pytest.fixture
    def orbs(self) -> list[Orb]:
        return [
            Orb(
                "Fine Delirium Orb",
                12,
                "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvRGVsaXJpdW0vRGVsaXJpdW1PcmJDdXJyZW5jeSIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/edac9239bd/DeliriumOrbCurrency.png",
            ),
            Orb(
                "Abyssal Delirium Orb",
                8,
                "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvRGVsaXJpdW0vRGVsaXJpdW1PcmJBYnlzcyIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/9c2b5d6d64/DeliriumOrbAbyss.png",
            ),
        ]

    def test_parse(self, orb_data, orbs):
        parsed_orbs = parse_orbs(orb_data)
        assert orbs[0] in parsed_orbs
        assert orbs[1] in parsed_orbs
