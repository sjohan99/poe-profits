import json
from urllib.parse import quote
from poe_profit_calc.globals import TRADE_BASE_URL, TRADE_URLS, League
from collections import defaultdict


class TradeLink:
    def __init__(
        self,
        name: str,
        type: str,
        identified: bool | None = None,
        min_ilvl: int | None = None,
        max_ilvl: int | None = None,
    ) -> None:
        base_query = defaultdict(dict)
        base_query.update(
            {
                "query": {
                    "status": {"option": "online"},
                    "name": name,
                    "type": type,
                    "stats": [{"type": "and", "filters": []}],
                    "filters": {
                        "misc_filters": {
                            "filters": self.build_filters(identified, min_ilvl, max_ilvl)
                        }
                    },
                },
                "sort": {"price": "asc"},
            }
        )
        self._query = quote(json.dumps(base_query))

    @staticmethod
    def build_filters(
        identified: bool | None = None, min_ilvl: int | None = None, max_ilvl: int | None = None
    ):
        filters = defaultdict(dict)
        if identified is not None:
            filters["identified"].update({"option": "true" if identified else "false"})
        if min_ilvl is not None:
            filters["ilvl"].update({"min": min_ilvl})
        if max_ilvl is not None:
            filters["ilvl"].update({"max": max_ilvl})
        return filters

    def get_link(self, league: League) -> str:
        base_url = TRADE_URLS[league]
        return f"{base_url}?q={self._query}"
