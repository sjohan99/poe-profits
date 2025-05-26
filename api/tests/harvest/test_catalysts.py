import pathlib
from poe_profit_calc.harvest.catalysts import Catalyst
import pytest
from poe_profit_calc.harvest.catalysts import parse_catalysts


class TestParseQuestions:
    @pytest.fixture(scope="session")
    def catalyst_data(self) -> bytes:
        file = pathlib.Path(pathlib.Path(__file__).parent, "data/currencyoverview_currency.json")
        with open(file, "rb") as f:
            return f.read()

    @pytest.fixture
    def catalysts(self) -> list[Catalyst]:
        return [
            Catalyst(
                "Prismatic Catalyst",
                9.75,
                "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvQ2F0YWx5c3RzL1ByaXNtYXRpY0NhdGFseXN0IiwidyI6MSwiaCI6MSwic2NhbGUiOjF9XQ/5e51d41a0e/PrismaticCatalyst.png",
                details_id="prismatic-catalyst",
            ),
            Catalyst(
                "Fertile Catalyst",
                6.54,
                "https://web.poecdn.com/gen/image/WzI1LDE0LHsiZiI6IjJESXRlbXMvQ3VycmVuY3kvQ2F0YWx5c3RzL0ZlcnRpbGVDYXRhbHlzdCIsInciOjEsImgiOjEsInNjYWxlIjoxfV0/4b4ca5d929/FertileCatalyst.png",
                details_id="fertile-catalyst",
            ),
        ]

    def test_parse_catalysts(self, catalyst_data, catalysts):
        parsed_orbs = parse_catalysts(catalyst_data)
        assert catalysts[0] in parsed_orbs
        assert catalysts[1] in parsed_orbs

    def test_parse_catalysts_assigns_icons(self, catalyst_data, catalysts):
        parsed_orbs = parse_catalysts(catalyst_data)
        pairs = []
        for catalyst in catalysts:
            for parsed_catalyst in parsed_orbs:
                if catalyst.name == parsed_catalyst.name:
                    pairs.append((catalyst, parsed_catalyst))
        c1, pc1 = pairs[0]
        c2, pc2 = pairs[1]
        assert c1.icon == pc1.icon
        assert c2.icon == pc2.icon
