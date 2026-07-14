"""
Backward compatibility layer for legacy provider loader.
"""

from app.ai.providers.base.registry import ProviderRegistry

registry = ProviderRegistry()


class ProviderLoader:
    def __init__(self):
        self.registry = registry

    def load(self, name, *args, **kwargs):
        if hasattr(self.registry, "get"):
            return self.registry.get(name)
        if hasattr(self.registry, "load"):
            return self.registry.load(name)
        if hasattr(self.registry, "create"):
            return self.registry.create(name)
        raise NotImplementedError("No compatible provider loading method found.")


# Legacy module-level singleton expected by older code
loader = ProviderLoader()


def load_provider(name, *args, **kwargs):
    return loader.load(name, *args, **kwargs)


__all__ = [
    "ProviderLoader",
    "loader",
    "registry",
    "load_provider",
]
