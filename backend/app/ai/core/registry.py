"""
Backward compatibility layer for legacy imports.
"""

from app.ai.providers.base.registry import (
    ProviderRegistry,
    AIProvider,
    Capability,
)

# Legacy aliases
Registry = ProviderRegistry
BaseRegistry = ProviderRegistry

# Legacy singleton expected by old code
registry = ProviderRegistry()

__all__ = [
    "ProviderRegistry",
    "Registry",
    "BaseRegistry",
    "registry",
    "AIProvider",
    "Capability",
]
