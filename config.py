"""Centralized application configuration using environment variables."""

from functools import lru_cache
from typing import Optional

from pydantic import AnyHttpUrl, Field, PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables or .env file."""

    # Core services
    database_url: PostgresDsn = Field(..., alias="DATABASE_URL")

    # Third-party integrations
    stripe_secret_key: Optional[str] = Field(None, alias="STRIPE_SECRET_KEY")
    stripe_publishable_key: Optional[str] = Field(None, alias="STRIPE_PUBLISHABLE_KEY")
    openai_api_key: Optional[str] = Field(None, alias="OPENAI_API_KEY")
    fan_engage_base_url: Optional[AnyHttpUrl] = Field(
        default=None, alias="FAN_ENGAGE_BASE_URL"
    )
    fan_engage_api_key: Optional[str] = Field(None, alias="FAN_ENGAGE_API_KEY")

    # Storage
    uploads_dir: str = Field("uploads", alias="UPLOADS_DIR")
    temp_dir: str = Field("temp", alias="TEMP_DIR")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    """Return a cached settings instance so downstream modules share it."""

    return Settings()


settings = get_settings()
