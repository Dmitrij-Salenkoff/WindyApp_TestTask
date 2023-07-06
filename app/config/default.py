"""File with settings"""
from os import environ

from pydantic import BaseSettings


class DefaultSettings(BaseSettings):
    """
    Default app settings
    """
    ENV: str = environ.get("ENV", "local")
    PATH_PREFIX: str = environ.get("PATH_PREFIX", "")
    APP_HOST: str = environ.get("APP_HOST", "localhost")
    APP_PORT: int = int(environ.get("APP_PORT", 8080))
    DATA_DIR_PATH: str = environ.get("DATA_PATH", "app/data/")
    HEADER_SIZE: int = int(environ.get("HEADER_SIZE", 8 * 4))


settings = DefaultSettings()
