from app.ai.providers.ollama_provider import OllamaProvider


def test_provider_metadata():
    provider = OllamaProvider()

    assert provider.name == "ollama"
    assert provider.model
    assert isinstance(provider.health(), bool)
