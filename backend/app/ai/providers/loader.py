from app.ai.providers.registry import registry
from app.ai.providers.mock_provider import MockAIProvider
from app.ai.providers.nvidia_provider import NVIDIAProvider
from app.ai.providers.ollama_provider import OllamaProvider


def load_providers() -> None:
    """
    Register all built-in AI providers.

    Safe to call multiple times.
    """

    providers = [
        MockAIProvider(),
        NVIDIAProvider(),
        OllamaProvider(),
    ]

    for provider in providers:
        try:
            registry.get(provider.name)
        except ValueError:
            registry.register(
                provider.name,
                provider,
            )
