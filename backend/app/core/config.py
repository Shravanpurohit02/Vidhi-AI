import os
from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Vidhi AI"
    APP_VERSION: str = "0.1.0-alpha.1"
    APP_ENV: str = "development"
    DEBUG: bool = True

    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = 8000

    SECRET_KEY: str = "change-me"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    JWT_ISSUER: str = "Vidhi-AI"
    JWT_AUDIENCE: str = "Vidhi-AI"
    ALGORITHM: str = "HS256"

    DATABASE_URL: str = "sqlite:///./vidhi_ai.db"

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )

    @field_validator("APP_ENV")
    @classmethod
    def validate_app_env(cls, value: str) -> str:
        value = value.lower()
        allowed = {"development", "testing", "staging", "production"}
        if value not in allowed:
            raise ValueError(f"APP_ENV must be one of: {', '.join(sorted(allowed))}")
        return value

    @field_validator("DEBUG")
    @classmethod
    def validate_debug(cls, value: bool, info):
        env = info.data.get("APP_ENV", "development").lower()
        if env == "production" and value:
            raise ValueError("DEBUG must be False when APP_ENV=production")
        return value


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
