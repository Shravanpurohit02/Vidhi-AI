from builder.kernel.context import KernelContext
from builder.kernel.state import KernelState

class Kernel:

    def __init__(self):
        self.context = KernelContext()
        self.state = KernelState()

kernel = Kernel()
