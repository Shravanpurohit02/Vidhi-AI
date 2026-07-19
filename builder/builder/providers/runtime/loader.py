import os
from pathlib import Path

from dotenv import dotenv_values

from builder.providers.runtime.catalog import PROVIDERS
from builder.providers.runtime.config import ProviderRuntime
from builder.providers.runtime.registry import registry


FILES = (
    Path.home() / "Vidhi-Builder/.env",
    Path.home() / "Vidhi-AI/backend/.env",
)


class ProviderLoader:

    def load(self):

        values = {}

        for file in FILES:
            if file.exists():
                values.update(dotenv_values(file))

        values.update(os.environ)

        registry.providers.clear()

        for provider in PROVIDERS:

            api_key = values.get(
                f"{provider.env_prefix}_API_KEY",
                "",
            )

            registry.register(
                ProviderRuntime(
                    name=provider.name,
                    display_name=provider.display_name,
                    api_type=provider.api_type,

                    api_key=api_key,

                    base_url=values.get(
                        f"{provider.env_prefix}_BASE_URL",
                        provider.default_base_url,
                    ),

                    model=values.get(
                        f"{provider.env_prefix}_MODEL",
                        provider.default_model,
                    ),

                    enabled=bool(api_key),

                    free_tier=provider.free_tier,
                    priority=provider.priority,

                    supports_streaming=provider.supports_streaming,
                    supports_tools=provider.supports_tools,
                    supports_vision=provider.supports_vision,
                    supports_reasoning=provider.supports_reasoning,
                    supports_embeddings=provider.supports_embeddings,

                    context_window=provider.context_window,
                    max_output_tokens=provider.max_output_tokens,
                )
            )

        return registry


loader = ProviderLoader()
