import logging
import sys

from fastapi import Depends, FastAPI
from poe_profit_calc.setup.logger import LoggingFormatter
from poe_profit_calc.setup.ratelimiting import RateLimiter
from poe_profit_calc.setup.settings import Settings, get_settings
from poe_profit_calc.vendor.request import Client, LocalClient

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
    settings: Settings
    client: Client

    def __init__(self):
        _settings = get_settings()
        initialize_logging(_settings)

        logging.info("Initializing app")

        if _settings.ENV == "prod":
            logging.info("Using HTTP Client")
            _client = Client(
                default_headers={"User-Agent": "poe-profits.com (+https://poe-profits.com/)"}
            )
        else:
            logging.info("Using Local File Client")
            path_prefix = _settings.LOCAL_FILE_PREFIX
            _client = LocalClient(path_prefix)

        rate_limiter = RateLimiter(
            requests_limit=_settings.REQUEST_LIMIT_PER_MINUTE, time_window=60, limit_globally=True
        )

        _app = FastAPI(dependencies=[Depends(rate_limiter)])
        App.app = _app
        App.settings = _settings
        App.client = _client

        logging.info(f"Initialized app in {_settings.ENV} mode")

    @staticmethod
    def get_instance():
        App()
        return App


def initialize_logging(settings: Settings):
    logFormatter = LoggingFormatter()
    logging_handlers = [
        logging.StreamHandler(sys.stdout),
    ]
    for handler in logging_handlers:
        handler.setFormatter(logFormatter)
    logging.basicConfig(level=logging.INFO, handlers=logging_handlers)

    # Suppress httpx info logs, they are too verbose, since they log every request we make
    # to third-party APIs, despite them being cached.
    logging.getLogger("httpx").setLevel(logging.WARNING)
