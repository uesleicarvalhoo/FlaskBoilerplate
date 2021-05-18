from typing import Union

from decouple import config


def _normalize_log_level(level: str) -> Union[str, int]:
    try:
        return int(level)
    except ValueError:
        return level.upper()


SECRET_KEY = config("SECRET_KEY")
BASE_PATH = config("BASE_PATH", default="")
SQLALCHEMY_DB_URI = config("SQLALCHEMY_DB_URI")

LOG_LEVEL = config("LOG_LEVEL", default="info", cast=_normalize_log_level)
WORKERS = config("WORKERS", default=2, cast=int)
HOST = config("HOST", default="0.0.0.0")
PORT = config("PORT", default=8000, cast=int)
