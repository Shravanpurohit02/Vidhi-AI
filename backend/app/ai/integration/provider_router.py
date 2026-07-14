from __future__ import annotations

from app.ai.providers.base.bootstrap import ProviderBootstrap
from app.ai.providers.base.router import CapabilityRouter


class ProviderRouter:

    def __init__(self):
        self.registry = ProviderBootstrap().build()
        self.router = CapabilityRouter(self.registry)

    def chat(self, *args, **kwargs):
        return self.router.chat(*args, **kwargs)

    def embed(self, *args, **kwargs):
        return self.router.embed(*args, **kwargs)

    def rerank(self, *args, **kwargs):
        return self.router.rerank(*args, **kwargs)

    def ocr(self, *args, **kwargs):
        return self.router.ocr(*args, **kwargs)

    def vision(self, *args, **kwargs):
        return self.router.vision(*args, **kwargs)

    def image_generation(self, *args, **kwargs):
        return self.router.image_generation(*args, **kwargs)

    def function_call(self, *args, **kwargs):
        return self.router.function_call(*args, **kwargs)

    def speech_to_text(self, *args, **kwargs):
        return self.router.speech_to_text(*args, **kwargs)

    def text_to_speech(self, *args, **kwargs):
        return self.router.text_to_speech(*args, **kwargs)

    def moderation(self, *args, **kwargs):
        return self.router.moderation(*args, **kwargs)


    def select(self, provider: str | None = None):
        return self.chat(provider=provider)


provider_router = ProviderRouter()
