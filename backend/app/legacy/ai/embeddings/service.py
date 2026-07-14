from __future__ import annotations

from app.ai.providers.base.bootstrap import ProviderBootstrap
from app.ai.providers.base.router import CapabilityRouter


class EmbeddingService:

    def __init__(self):
        registry = ProviderBootstrap().build()
        self.router = CapabilityRouter(registry)

    def create(
        self,
        text: str,
        provider: str | None = None,
    ) -> list[float]:
        return self.router.embed(
            text=text,
            preferred_provider=provider,
        )

    def batch(
        self,
        texts: list[str],
        provider: str | None = None,
    ) -> list[list[float]]:
        return [
            self.create(
                text,
                provider,
            )
            for text in texts
        ]
