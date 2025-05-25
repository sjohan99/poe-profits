from fastapi.testclient import TestClient
from poe_profit_calc.routers import gems
from poe_profit_calc.setup.setup import App
from snapshots.utils import sort_and_round_json

PARAMS = {
    "league": "Standard",
}
BASE_URL = "/gems"


app = App.get_instance().app
app.include_router(gems.router)
client = TestClient(app)


def test_get_summary(snapshot):
    response = client.get(f"{BASE_URL}/summary", params=PARAMS)
    assert response.status_code == 200
    assert sort_and_round_json(response.json()) == snapshot
