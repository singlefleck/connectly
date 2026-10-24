from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="CONNECTLY_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Connectly API"
    app_description: str = (
        "Backend API for the Connectly video calling application."
    )
    app_version: str = "0.1.0"
    debug: bool = False


@lru_cache
def get_settings() -> Settings:
    return Settings()