"""
Backward compatibility layer for legacy routing API.
"""

from enum import Enum

from app.ai.core.router import AIRouter, router


class RoutingMode(str, Enum):
    AUTO = "auto"
    MANUAL = "manual"


class RoutingPolicy:
    def __init__(self, mode: RoutingMode = RoutingMode.AUTO):
        self.mode = mode


__all__ = [
    "AIRouter",
    "router",
    "RoutingMode",
    "RoutingPolicy",
]
