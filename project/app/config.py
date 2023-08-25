# project/app/config.py


import logging
from functools import lru_cache

from pydantic import BaseSettings


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)
    zaxier: str = "zaxier"


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
