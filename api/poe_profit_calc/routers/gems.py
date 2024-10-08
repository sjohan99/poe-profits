from cachetools import TTLCache, cached
from fastapi import APIRouter
from poe_profit_calc.gemlevelling import GemProfit, GemType, create_profitability_report, parse
from poe_profit_calc.setup.setup import App
from poe_profit_calc.sources import PoeNinjaSource
from pydantic import BaseModel

router = APIRouter(
    prefix="/gems",
)

price_fetcher = App.get_instance().price_fetcher


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
@cached(cache=TTLCache(maxsize=128, ttl=1800))
def get_gem_summary() -> list[GemData]:
    raw_data = price_fetcher.get_raw_endpoint(PoeNinjaSource.SKILL_GEM)
    parsed_data = parse(raw_data)
    pr = create_profitability_report(parsed_data)
    result = [GemData.from_gem(gem) for gem in pr]
    result.sort(key=lambda x: x.level_profit, reverse=True)
    return result
