import logging
import sys

from fastapi import Depends, FastAPI
from poe_profit_calc.globals import League
from poe_profit_calc.fetcher import FileFetcher, HttpFetcher
from poe_profit_calc.prices import Pricer
from poe_profit_calc.setup.logger import LoggingFormatter
from poe_profit_calc.setup.ratelimiting import RateLimiter
from poe_profit_calc.setup.settings import Settings, get_settings
from poe_profit_calc.sources import FILE_PATH_MAPPING, make_endpoint_mapping

from threading import Lock


class SingletonMeta(type):
    """
    Thread-safe implementation of Singleton.
    """

    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class App(metaclass=SingletonMeta):

    app: FastAPI
    price_fetchers: dict[League, Pricer]
    settings: Settings

    def __init__(self):
        initialize_logging()
        _settings = get_settings()

        logging.info(f"Initializing app")

        if _settings.ENV == "prod":
            logging.info("Using HTTP fetcher")
            fetcher = HttpFetcher()
            _price_fetchers = {
                league: Pricer(fetcher=fetcher, source_mapping=make_endpoint_mapping(league))
                for league in League
            }
        else:
            logging.info("Using file fetcher")
            pricer = Pricer(fetcher=FileFetcher(), source_mapping=FILE_PATH_MAPPING)
            _price_fetchers = {league: pricer for league in League}

        rate_limiter = RateLimiter(
            requests_limit=_settings.REQUEST_LIMIT_PER_MINUTE, time_window=60, limit_globally=True
        )

        _app = FastAPI(dependencies=[Depends(rate_limiter)])
        App.app = _app
        App.price_fetchers = _price_fetchers
        App.settings = _settings

        logging.info(f"Initialized app in {_settings.ENV} mode")

    @staticmethod
    def get_instance():
        App()
        return App


def initialize_logging():
    logFormatter = LoggingFormatter()
    logging_handlers = [
        logging.StreamHandler(sys.stdout),
    ]
    for handler in logging_handlers:
        handler.setFormatter(logFormatter)
    logging.basicConfig(level=logging.INFO, handlers=logging_handlers)
