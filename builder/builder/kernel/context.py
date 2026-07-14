from dataclasses import dataclass, field
from uuid import uuid4

@dataclass(slots=True)
class KernelContext:
    id: str = field(default_factory=lambda: uuid4().hex)
    project: str = ""
    workspace: str = ""
    runtime_id: str = ""
