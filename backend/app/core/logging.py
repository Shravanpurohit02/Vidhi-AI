from __future__ import annotations

from pathlib import Path
import sys

from loguru import logger

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.remove()

logger.add(
    LOG_DIR / "vidhi_ai.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
)

logger.add(
    sys.stdout,
    level="INFO",
)


def get_logger(
    name: str | None = None,
):
    """
    Return the application's shared logger.

    If a module name is supplied, return a logger bound to that module.
    Existing calls to get_logger() continue to work unchanged.
    """

    if name:
        return logger.bind(module=name)

    return logger
