from app.ai.providers.base.router import CapabilityRouter

# Compatibility aliases
FailoverManager = CapabilityRouter
ProviderFailover = CapabilityRouter
Failover = CapabilityRouter

# Legacy singleton expected by older imports
failover = CapabilityRouter

__all__ = [
    "FailoverManager",
    "ProviderFailover",
    "Failover",
    "failover",
]
