from dataclasses import dataclass, field
from uuid import uuid4

@dataclass(slots=True)
class ExecutionContext:
    id: str = field(default_factory=lambda: uuid4().hex)
    plan_id: str = ""
    worker_id: str = ""
    job_id: str = ""
