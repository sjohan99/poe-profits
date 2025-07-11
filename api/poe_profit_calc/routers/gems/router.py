from fastapi import APIRouter, HTTPException
from poe_profit_calc.gemlevelling import GemProfit, GemType, create_profitability_report, parse
from poe_profit_calc.globals import League
from poe_profit_calc.setup.setup import App
from poe_profit_calc.vendor.request import PoeNinjaEndpoint as pne
from pydantic import BaseModel

router = APIRouter(
    prefix="/gems",
)


class GemData(BaseModel):
    name: str
    level_profit: float
    level_c_profit: float | None
    level_q_c_profit: float | None
    xp_adjusted_level_profit: float
    xp_adjusted_c_profit: float | None
    xp_adjusted_q_c_profit: float | None
    vaal_orb_profit: float | None
    vaal_orb_20q_profit: float | None
    vaal_level_profit: float | None
    gem_type: GemType
    img: str | None

    @staticmethod
    def from_gem(gem_profit: GemProfit):
        return GemData(
            name=gem_profit.gem.name,
            level_profit=gem_profit.level_profit,
            level_c_profit=gem_profit.level_c_profit,
            level_q_c_profit=gem_profit.level_q_c_profit,
            xp_adjusted_level_profit=gem_profit.xp_adjusted_level_profit,
            xp_adjusted_c_profit=gem_profit.xp_adjusted_c_profit,
            xp_adjusted_q_c_profit=gem_profit.xp_adjusted_q_c_profit,
            vaal_orb_profit=gem_profit.vaal_orb_profit,
            vaal_orb_20q_profit=gem_profit.vaal_orb_20q_profit,
            vaal_level_profit=gem_profit.vaal_level_profit,
            gem_type=gem_profit.gem.type,
            img=gem_profit.gem.icon,
        )


@router.get("/summary")
async def get_gem_summary_async(league: League) -> list[GemData]:
    raw_data = await App.get_instance().client.request_endpoint(
        pne.SKILL_GEM,
        league,
    )
    if raw_data is None:
        raise HTTPException(
            status_code=503, detail="Failed to fetch gem data: third-party resource unavailable."
        )
    parsed_data = parse(raw_data)
    pr = create_profitability_report(parsed_data)
    result = [GemData.from_gem(gem) for gem in pr]
    result.sort(key=lambda x: x.level_profit, reverse=True)
    return result
