"""
Legacy compatibility layer.
"""

from app.ai.providers.base.health_manager import ProviderHealthManager

health_monitor = ProviderHealthManager()
health_manager = health_monitor
monitor = health_monitor


class HealthMonitor(ProviderHealthManager):
    pass


__all__ = [
    "ProviderHealthManager",
    "HealthMonitor",
    "health_monitor",
    "health_manager",
    "monitor",
]
