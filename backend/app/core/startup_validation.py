from pathlib import Path

from app.core.config import settings


def validate_startup() -> None:
    if settings.APP_ENV.lower() != "production":
        return

    placeholder_keys = {
        "",
        "CHANGE_WITH_A_LONG_RANDOM_SECRET",
        "replace-with-a-long-random-secret",
    }

    if settings.SECRET_KEY in placeholder_keys:
        raise RuntimeError("Production SECRET_KEY has not been configured.")

    if settings.DEBUG:
        raise RuntimeError("DEBUG must be False in production.")

    storage = Path("storage")
    logs = Path("logs")

    storage.mkdir(parents=True, exist_ok=True)
    logs.mkdir(parents=True, exist_ok=True)

    if not storage.is_dir():
        raise RuntimeError("storage directory unavailable")

    if not logs.is_dir():
        raise RuntimeError("logs directory unavailable")
