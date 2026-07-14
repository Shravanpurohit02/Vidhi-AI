from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ProviderCost:

    input_per_million_tokens: float = 0.0
    output_per_million_tokens: float = 0.0

    def estimate(
        self,
        input_tokens: int,
        output_tokens: int = 0,
    ) -> float:

        return (
            (input_tokens / 1_000_000) * self.input_per_million_tokens
            +
            (output_tokens / 1_000_000) * self.output_per_million_tokens
        )


class CostManager:

    def __init__(self):
        self.providers: dict[str, ProviderCost] = {}

    def register(
        self,
        provider: str,
        input_cost: float,
        output_cost: float,
    ) -> None:

        self.providers[provider] = ProviderCost(
            input_per_million_tokens=input_cost,
            output_per_million_tokens=output_cost,
        )

    def estimate(
        self,
        provider: str,
        input_tokens: int,
        output_tokens: int = 0,
    ) -> float:

        cost = self.providers.get(provider)

        if cost is None:
            return 0.0

        return cost.estimate(
            input_tokens,
            output_tokens,
        )
