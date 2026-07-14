from __future__ import annotations

from app.ai.providers.base.bootstrap import ProviderBootstrap
from app.ai.providers.base.router import CapabilityRouter


class AIService:

    def __init__(self):
        self.registry = ProviderBootstrap().build()
        self.router = CapabilityRouter(self.registry)

    def chat_provider(self):
        return self.router

    def streaming_provider(self):
        return self.router

    def embedding_provider(self):
        return self.router

    def json_provider(self):
        return self.router

    def provider(
        self,
        capability=None,
        preferred=None,
    ):
        return self.router

    def available(self):
        return [
            p.name
            for p in self.registry.providers()
            if p.health()
        ]

    def health(self):
        return {
            p.name: p.health()
            for p in self.registry.providers()
        }


ai_service = AIService()
