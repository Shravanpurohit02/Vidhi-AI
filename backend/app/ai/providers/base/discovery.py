from __future__ import annotations

import os

from app.ai.providers.base.registry import ProviderRegistry


class ProviderDiscovery:

    ENV_MAP = {
        "OPENAI_API_KEY": "openai",
        "NVIDIA_API_KEY": "nvidia",
        "GOOGLE_API_KEY": "gemini",
        "GROQ_API_KEY": "groq",
        "ANTHROPIC_API_KEY": "anthropic",
        "OPENROUTER_API_KEY": "openrouter",
        "MISTRAL_API_KEY": "mistral",
        "CEREBRAS_API_KEY": "cerebras",
        "HUGGINGFACE_API_KEY": "huggingface",
    }

    def available(self):

        return [
            provider
            for env, provider in self.ENV_MAP.items()
            if os.getenv(env)
        ]

    def register_available(
        self,
        registry: ProviderRegistry,
    ):
        return self.available()
