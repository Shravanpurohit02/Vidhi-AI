from __future__ import annotations

from abc import ABC
from app.ai.providers.capabilities import Capability


class AIProvider(ABC):

    name: str = ""
    priority: int = 100
    enabled: bool = True

    capabilities: set[Capability] = set()

    def supports(self, capability: Capability) -> bool:
        return capability in self.capabilities

    def health(self) -> bool:
        return True

    def chat(self, *args, **kwargs):
        raise NotImplementedError

    def embed(self, *args, **kwargs):
        raise NotImplementedError

    def rerank(self, *args, **kwargs):
        raise NotImplementedError

    def ocr(self, *args, **kwargs):
        raise NotImplementedError

    def vision(self, *args, **kwargs):
        raise NotImplementedError

    def image_generation(self, *args, **kwargs):
        raise NotImplementedError

    def function_call(self, *args, **kwargs):
        raise NotImplementedError

    def speech_to_text(self, *args, **kwargs):
        raise NotImplementedError

    def text_to_speech(self, *args, **kwargs):
        raise NotImplementedError

    def moderation(self, *args, **kwargs):
        raise NotImplementedError
