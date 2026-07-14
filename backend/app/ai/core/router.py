"""
Backward compatibility layer for legacy AI router.
"""

from app.ai.providers.base.router import (
    CapabilityRouter,
    Capability,
    ProviderRegistry,
    ProviderHealthManager,
    ProviderMetrics,
)

_registry = ProviderRegistry()
router = CapabilityRouter(_registry)


class AIRouter(CapabilityRouter):
    def __init__(self):
        super().__init__(_registry)


__all__ = [
    "AIRouter",
    "CapabilityRouter",
    "Capability",
    "ProviderRegistry",
    "ProviderHealthManager",
    "ProviderMetrics",
    "router",
]
