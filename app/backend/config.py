from pathlib import Path
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


class Config(BaseConfig):
    POSTGRES_URL: str
    TEST_POSTGRES_URL: str


config: Config = Config()
