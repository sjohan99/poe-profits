from fastapi.responses import RedirectResponse
from poe_profit_calc.routers import bosses, gems, harvest
from poe_profit_calc.setup.setup import App

app = App.get_instance().app
app.include_router(bosses.router)
app.include_router(gems.router)
app.include_router(harvest.router)


@app.get("/", include_in_schema=False)
async def main_route():
    return RedirectResponse(url="/docs")
