from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4


@dataclass
class Job:
    id: str = field(default_factory=lambda: str(uuid4()))
    name: str = ""
    status: str = "queued"
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    payload: dict = field(default_factory=dict)
