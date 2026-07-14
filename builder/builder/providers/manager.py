from builder.providers.provider import MockProvider
from builder.providers.registry import registry

class ProviderManager:

    def __init__(self):
        registry.register(MockProvider())

    def generate(self, request):
        provider = registry.get(request.model)
        return provider.generate(request)

manager = ProviderManager()
