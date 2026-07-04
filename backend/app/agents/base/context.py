from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentContext:
    user_id: int | None = None
    session_id: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
