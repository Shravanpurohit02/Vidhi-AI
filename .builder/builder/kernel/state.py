from dataclasses import dataclass

@dataclass(slots=True)
class KernelState:
    initialized: bool = False
    running: bool = False
    cycles: int = 0
