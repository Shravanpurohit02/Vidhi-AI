from __future__ import annotations

from datetime import UTC, datetime, timedelta


class ProviderHealthManager:

    def __init__(self):
        self._status = {}

    def healthy(self, provider: str) -> bool:

        info = self._status.get(provider)

        if info is None:
            return True

        if info["healthy"]:
            return True

        return datetime.now(UTC) >= info["retry_at"]

    def mark_success(self, provider: str):

        self._status[provider] = {
            "healthy": True,
            "retry_at": datetime.now(UTC),
        }

    def mark_failure(
        self,
        provider: str,
        retry_after: int = 60,
    ):

        self._status[provider] = {
            "healthy": False,
            "retry_at": datetime.now(UTC)
            + timedelta(seconds=retry_after),
        }
