import os
from pathlib import Path

from dotenv import dotenv_values

from builder.providers.runtime.config import ProviderRuntime
from builder.providers.runtime.registry import registry

FILES = [
    Path.home() / "Vidhi-Builder/.env",
    Path.home() / "Vidhi-AI/backend/.env",
]

class ProviderLoader:

    def load(self):
        values = {}

        for file in FILES:
            if file.exists():
                values.update(dotenv_values(file))

        values.update(os.environ)

        providers = [
            ("nvidia","NVIDIA"),
            ("groq","GROQ"),
            ("gemini","GOOGLE"),
            ("openrouter","OPENROUTER"),
            ("cerebras","CEREBRAS"),
            ("mistral","MISTRAL"),
            ("anthropic","ANTHROPIC"),
            ("openai","OPENAI"),
            ("huggingface","HUGGINGFACE"),
        ]

        registry.providers.clear()

        for name,prefix in providers:
            registry.register(
                ProviderRuntime(
                    name=name,
                    api_key=values.get(f"{prefix}_API_KEY",""),
                    base_url=values.get(f"{prefix}_BASE_URL",""),
                    model=values.get(f"{prefix}_MODEL",""),
                    enabled=bool(values.get(f"{prefix}_API_KEY")),
                )
            )

        return registry

loader = ProviderLoader()
