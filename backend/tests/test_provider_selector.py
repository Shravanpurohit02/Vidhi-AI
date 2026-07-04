from app.ai.providers.loader import load_providers
from app.ai.providers.provider_selector import selector


def test_selector_returns_provider():
    load_providers()

    provider = selector.select()

    assert provider is not None
    assert provider.name in (
        "mock",
        "ollama",
        "nvidia",
    )
