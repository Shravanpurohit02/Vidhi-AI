"""
Backward compatibility layer.

Legacy modules import:
    from app.ai.core.provider import Provider

Current implementation exposes:
    AIProvider
"""

from app.ai.providers.base.provider import AIProvider, Capability

Provider = AIProvider
BaseProvider = AIProvider

__all__ = [
    "Provider",
    "BaseProvider",
    "AIProvider",
    "Capability",
]
