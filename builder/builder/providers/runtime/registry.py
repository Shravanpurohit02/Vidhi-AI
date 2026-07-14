class RuntimeRegistry:

    def __init__(self):
        self.providers = {}

    def register(self, provider):
        self.providers[provider.name] = provider

    def get(self, name):
        return self.providers.get(name)

    def all(self):
        return list(self.providers.values())

registry = RuntimeRegistry()
