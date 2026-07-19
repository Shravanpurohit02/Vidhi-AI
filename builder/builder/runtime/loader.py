from builder.runtime.introspection import inspector
from builder.runtime.registry import registry


class RuntimeLoader:

    def load(self):
        if registry.runtime is not None:
            return registry.runtime, registry.manifest

        runtime, manifest = inspector.inspect()

        registry.runtime = runtime
        registry.manifest = manifest

        return runtime, manifest


loader = RuntimeLoader()
