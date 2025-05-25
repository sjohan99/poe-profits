from fastapi.testclient import TestClient
from poe_profit_calc.routers import harvest
from poe_profit_calc.setup.setup import App
from snapshots.utils import sort_and_round_json

PARAMS = {
    "league": "Standard",
}
BASE_URL = "/harvest"


app = App.get_instance().app
app.include_router(harvest.router)
client = TestClient(app)


def test_get_orbs(snapshot):
    response = client.get(f"{BASE_URL}/orbs", params=PARAMS)
    assert response.status_code == 200
    assert sort_and_round_json(response.json()) == snapshot


def test_get_catalyts(snapshot):
    response = client.get(f"{BASE_URL}/catalysts", params=PARAMS)
    assert response.status_code == 200
    assert sort_and_round_json(response.json()) == snapshot


def test_get_overview(snapshot):
    response = client.get(f"{BASE_URL}/overview", params=PARAMS)
    assert response.status_code == 200
    assert sort_and_round_json(response.json()) == snapshot
