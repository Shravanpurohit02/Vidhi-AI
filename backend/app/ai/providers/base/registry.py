from __future__ import annotations

from collections import defaultdict

from app.ai.providers.base.provider import AIProvider
from app.ai.providers.capabilities import Capability


class ProviderRegistry:

    def __init__(self):

        self.providers: dict[str, AIProvider] = {}

    def register(
        self,
        provider: AIProvider,
    ) -> None:

        self.providers[provider.name] = provider

    def get(
        self,
        name: str,
    ) -> AIProvider:

        return self.providers[name]

    def all(self) -> list[AIProvider]:

        return list(self.providers.values())

    def by_capability(
        self,
        capability: Capability,
    ) -> list[AIProvider]:

        providers = [
            p for p in self.providers.values()
            if p.enabled
            and p.health()
            and p.supports(capability)
        ]

        providers.sort(
            key=lambda p: p.priority
        )

        return providers

    def capabilities(self):

        result = defaultdict(list)

        for provider in self.providers.values():

            for capability in provider.capabilities:
                result[capability.value].append(provider.name)

        return dict(result)
