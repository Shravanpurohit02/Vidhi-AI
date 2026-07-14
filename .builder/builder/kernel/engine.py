from builder.runtime import loader

from .kernel import kernel
from .registry import registry

class KernelEngine:

    def boot(self):
        runtime, _ = loader.load()

        kernel.context.project = runtime.project
        kernel.context.workspace = runtime.workspace
        kernel.context.runtime_id = runtime.id

        kernel.state.initialized = True
        kernel.state.running = True
        kernel.state.cycles += 1

        registry.kernel = kernel

        return kernel

engine = KernelEngine()
