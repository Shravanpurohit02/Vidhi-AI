"""
Backward compatibility layer for the legacy ProviderManager.
"""

from app.ai.providers.base.registry import ProviderRegistry

registry = ProviderRegistry()


class ProviderManager:
    def __init__(self):
        self.registry = registry

    def get(self, name, *args, **kwargs):
        if hasattr(self.registry, "get"):
            return self.registry.get(name)
        if hasattr(self.registry, "load"):
            return self.registry.load(name)
        if hasattr(self.registry, "create"):
            return self.registry.create(name)
        raise NotImplementedError("No compatible provider lookup method found.")

    load = get
    create = get


manager = ProviderManager()

__all__ = [
    "ProviderManager",
    "manager",
]
