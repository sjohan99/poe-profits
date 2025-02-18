from fastapi import APIRouter
from poe_profit_calc.globals import League

router = APIRouter(
    prefix="/metadata",
)


@router.get("/leagues")
def get_leagues() -> list[League]:
    return [league for league in League]
