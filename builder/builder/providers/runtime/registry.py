class RuntimeRegistry:

    def __init__(self):
        self.providers = {}

    #
    # Existing API
    #

    def register(self, provider):
        self.providers[provider.name] = provider

    def get(self, name):
        return self.providers.get(name)

    def all(self):
        return list(self.providers.values())

    #
    # Capability Queries
    #

    def enabled(self):
        return [
            p
            for p in self.providers.values()
            if p.enabled
        ]

    def healthy(self):
        return [
            p
            for p in self.enabled()
            if p.healthy
        ]

    def free(self):
        return [
            p
            for p in self.enabled()
            if p.free_tier
        ]

    def compatible(self, api_type):
        return [
            p
            for p in self.enabled()
            if p.api_type == api_type
        ]

    def supports(self, capability):

        attribute = f"supports_{capability}"

        return [
            p
            for p in self.enabled()
            if getattr(
                p,
                attribute,
                False,
            )
        ]

    #
    # Selection
    #

    def highest_priority(self):

        providers = sorted(
            self.enabled(),
            key=lambda p: p.priority,
        )

        return (
            providers[0]
            if providers
            else None
        )

    def best(self):

        providers = sorted(
            self.healthy(),
            key=lambda p: (
                p.priority,
                not p.free_tier,
                p.failure_count,
                -p.success_rate,
                p.average_latency,
            ),
        )

        return (
            providers[0]
            if providers
            else None
        )


registry = RuntimeRegistry()
