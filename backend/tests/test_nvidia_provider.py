from app.ai.providers.nvidia_provider import NVIDIAProvider


def test_provider():

    provider = NVIDIAProvider()

    assert provider.name == "nvidia"

    assert provider.model

    assert isinstance(
        provider.health(),
        bool,
    )
