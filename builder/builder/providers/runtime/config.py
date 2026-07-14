from dataclasses import dataclass

@dataclass(slots=True)
class ProviderRuntime:
    name: str
    api_key: str
    base_url: str
    model: str
    enabled: bool
