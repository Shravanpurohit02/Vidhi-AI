from builder.models.kernel import Kernel

class BuilderKernel:

    def __init__(self):
        self.kernel = Kernel()

    def start(self):
        self.kernel.running = True
        return self.kernel

    def stop(self):
        self.kernel.running = False

    def status(self):
        return self.kernel

kernel = BuilderKernel()
