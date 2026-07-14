from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ProviderMetrics:
    requests: int = 0
    successes: int = 0
    failures: int = 0
    avg_latency_ms: float = 0.0

    def record(
        self,
        latency_ms: float,
        success: bool,
    ) -> None:

        self.requests += 1

        if success:
            self.successes += 1
        else:
            self.failures += 1

        self.avg_latency_ms = (
            (self.avg_latency_ms * (self.requests - 1))
            + latency_ms
        ) / self.requests

    @property
    def success_rate(self) -> float:
        if self.requests == 0:
            return 1.0
        return self.successes / self.requests
