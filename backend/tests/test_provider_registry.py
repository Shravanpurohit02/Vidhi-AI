from app.ai.providers.mock_provider import MockAIProvider
from app.ai.providers.registry import registry


def test_registry():

    registry.register(
        "mock_test",
        MockAIProvider(),
    )

    provider = registry.get("mock_test")

    assert provider is not None
    assert "mock_test" in registry.providers()
