from app.ai.providers.mock_provider import MockAIProvider


def test_mock_provider_metadata():
    provider = MockAIProvider()

    assert provider.name == "mock"
    assert provider.model == "mock-model"
    assert provider.health() is True
