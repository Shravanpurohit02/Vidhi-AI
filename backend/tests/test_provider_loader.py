from app.ai.providers.loader import load_providers
from app.ai.providers.registry import registry


def test_loader_registers_default_providers():
    load_providers()

    providers = registry.providers()

    assert "mock" in providers
    assert "nvidia" in providers
    assert "ollama" in providers
