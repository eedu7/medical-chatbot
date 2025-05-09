from pathlib import Path
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


class Config(BaseConfig):
    POSTGRES_URL: PostgresDsn = (
        "postgresql+asyncpg://postgres:password123@127.0.0.1:5432/fastapi-db"
    )
    TEST_POSTGRES_URL: PostgresDsn = (
        "postgresql://postgres:password123@127.0.0.1:5431/db-test"
    )
    RELEASE_VERSION: str = "0.0.1"
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # One Day
    JWT_REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # Seven Day


config: Config = Config()
