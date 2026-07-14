from builder.providers.runtime.loader import loader

class ProviderRouter:

    def available(self):
        return [
            p
            for p in loader.load().all()
            if p.enabled
        ]

    def default(self):
        available = self.available()
        return available[0] if available else None

router = ProviderRouter()
