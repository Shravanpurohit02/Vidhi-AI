from __future__ import annotations

import time

from app.ai.providers.base.health_manager import ProviderHealthManager
from app.ai.providers.base.metrics import ProviderMetrics
from app.ai.providers.base.registry import ProviderRegistry
from app.ai.providers.capabilities import Capability


class CapabilityRouter:

    def __init__(self, registry: ProviderRegistry):
        self.registry = registry
        self.health = ProviderHealthManager()
        self.metrics: dict[str, ProviderMetrics] = {}

    def _metric(self, provider):
        return self.metrics.setdefault(
            provider.name,
            ProviderMetrics(),
        )

    def execute(self, capability: Capability, method: str, *args, **kwargs):
        providers = self.registry.by_capability(capability)
        last_error = None

        for provider in providers:

            if not self.health.healthy(provider.name):
                continue

            started = time.perf_counter()

            try:
                result = getattr(provider, method)(*args, **kwargs)

                latency = (time.perf_counter() - started) * 1000

                self._metric(provider).record(latency, True)
                self.health.mark_success(provider.name)

                return result

            except Exception as exc:

                latency = (time.perf_counter() - started) * 1000

                self._metric(provider).record(latency, False)
                self.health.mark_failure(provider.name)

                last_error = exc

        raise RuntimeError(
            f"No healthy provider available for {capability.value}"
        ) from last_error

    def chat(self,*a,**k):
        return self.execute(Capability.CHAT,"chat",*a,**k)

    def embed(self,*a,**k):
        return self.execute(Capability.EMBEDDING,"embed",*a,**k)

    def rerank(self,*a,**k):
        return self.execute(Capability.RERANK,"rerank",*a,**k)

    def ocr(self,*a,**k):
        return self.execute(Capability.OCR,"ocr",*a,**k)

    def vision(self,*a,**k):
        return self.execute(Capability.VISION,"vision",*a,**k)

    def image_generation(self,*a,**k):
        return self.execute(Capability.IMAGE_GENERATION,"image_generation",*a,**k)

    def function_call(self,*a,**k):
        return self.execute(Capability.FUNCTION_CALLING,"function_call",*a,**k)

    def speech_to_text(self,*a,**k):
        return self.execute(Capability.SPEECH_TO_TEXT,"speech_to_text",*a,**k)

    def text_to_speech(self,*a,**k):
        return self.execute(Capability.TEXT_TO_SPEECH,"text_to_speech",*a,**k)

    def moderation(self,*a,**k):
        return self.execute(Capability.MODERATION,"moderation",*a,**k)
