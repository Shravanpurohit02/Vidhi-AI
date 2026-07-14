from __future__ import annotations

import importlib
import logging

from app.ai.providers.base.discovery import ProviderDiscovery
from app.ai.providers.base.registry import ProviderRegistry

logger = logging.getLogger(__name__)


class ProviderBootstrap:

    PROVIDERS = {
        "nvidia": (
            "app.ai.providers.llm.nvidia_provider",
            "NVIDIAProvider",
        ),
        "openai": (
            "app.ai.providers.llm.openai_provider",
            "OpenAIProvider",
        ),
        "gemini": (
            "app.ai.providers.llm.gemini_provider",
            "GeminiProvider",
        ),
        "anthropic": (
            "app.ai.providers.llm.anthropic_provider",
            "AnthropicProvider",
        ),
        "groq": (
            "app.ai.providers.llm.groq_provider",
            "GroqProvider",
        ),
        "openrouter": (
            "app.ai.providers.llm.openrouter_provider",
            "OpenrouterProvider",
        ),
        "mistral": (
            "app.ai.providers.llm.mistral_provider",
            "MistralProvider",
        ),
        "cerebras": (
            "app.ai.providers.llm.cerebras_provider",
            "CerebrasProvider",
        ),
        "huggingface": (
            "app.ai.providers.embeddings.huggingface_provider",
            "HuggingFaceProvider",
        ),
    }

    def build(self):

        registry = ProviderRegistry()

        available = set(
            ProviderDiscovery().available()
        )

        for name in available:

            spec = self.PROVIDERS.get(name)

            if spec is None:
                continue

            module_name, class_name = spec

            try:

                module = importlib.import_module(module_name)

                provider = getattr(
                    module,
                    class_name,
                )()

                registry.register(provider)

            except Exception as exc:

                logger.warning(
                    "Skipping provider %s: %s",
                    name,
                    exc,
                )

        return registry
