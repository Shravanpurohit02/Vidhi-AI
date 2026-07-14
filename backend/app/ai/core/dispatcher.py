from app.ai.providers.base.router import CapabilityRouter

# Legacy compatibility aliases
Dispatcher = CapabilityRouter
RequestDispatcher = CapabilityRouter
ProviderDispatcher = CapabilityRouter
AIDispatcher = CapabilityRouter

dispatcher = CapabilityRouter
request_dispatcher = CapabilityRouter

__all__ = [
    "Dispatcher",
    "RequestDispatcher",
    "ProviderDispatcher",
    "AIDispatcher",
    "dispatcher",
    "request_dispatcher",
]
