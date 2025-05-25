from fastapi.testclient import TestClient
from poe_profit_calc.routers import bosses
from poe_profit_calc.setup.setup import App

import pytest
from snapshots.utils import sort_and_round_json

PARAMS = {
    "league": "Standard",
}
BASE_URL = "/bosses"
BOSS_IDS = {
    "the_searing_exarch",
    "the_searing_exarch_uber",
    "the_eater_of_worlds",
    "the_eater_of_worlds_uber",
    "the_shaper",
    "the_shaper_uber",
    "the_elder",
    "the_elder_uber",
    "the_elder_uber_uber",
    "sirus",
    "sirus_uber",
    "the_maven",
    "the_maven_uber",
    "venarius",
    "venarius_uber",
}

app = App.get_instance().app
app.include_router(bosses.router)
client = TestClient(app)


@pytest.mark.parametrize("boss_id", BOSS_IDS)
def test_get_boss(snapshot, boss_id):
    response = client.get(f"{BASE_URL}/boss/{boss_id}", params=PARAMS)
    assert response.status_code == 200
    assert sort_and_round_json(response.json()) == snapshot


def test_get_boss_all(snapshot):
    response = client.get(f"{BASE_URL}/all", params=PARAMS)
    assert response.status_code == 200
    assert sort_and_round_json(response.json()) == snapshot


def test_get_boss_summary(snapshot):
    response = client.get(f"{BASE_URL}/summary", params=PARAMS)
    assert response.status_code == 200
    assert sort_and_round_json(response.json()) == snapshot
