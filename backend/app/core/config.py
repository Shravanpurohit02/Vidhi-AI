from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Vidhi AI"
    APP_VERSION: str = "0.1.0-alpha.1"
    APP_ENV: str = "development"
    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    SECRET_KEY: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"

    DATABASE_URL: str = "sqlite:///./vidhi_ai.db"

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
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
