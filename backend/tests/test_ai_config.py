from app.ai.config import DEFAULT_PROVIDER

def test_default_provider():
    assert isinstance(DEFAULT_PROVIDER, str)
