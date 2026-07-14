from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ProviderQuota:

    daily_limit: int = 0
    used: int = 0

    @property
    def remaining(self) -> int:
        if self.daily_limit <= 0:
            return 10**18
        return max(0, self.daily_limit - self.used)

    def available(self) -> bool:
        return self.remaining > 0

    def consume(self, amount: int = 1) -> None:
        self.used += amount


class QuotaManager:

    def __init__(self):
        self.providers: dict[str, ProviderQuota] = {}

    def register(
        self,
        provider: str,
        daily_limit: int = 0,
    ) -> None:
        self.providers.setdefault(
            provider,
            ProviderQuota(daily_limit=daily_limit),
        )

    def available(
        self,
        provider: str,
    ) -> bool:
        quota = self.providers.get(provider)
        return quota is None or quota.available()

    def consume(
        self,
        provider: str,
        amount: int = 1,
    ) -> None:
        quota = self.providers.get(provider)
        if quota:
            quota.consume(amount)
