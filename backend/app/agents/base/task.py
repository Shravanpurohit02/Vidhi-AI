from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentTask:
    objective: str
    steps: list[str] = field(default_factory=list)
    parameters: dict[str, Any] = field(default_factory=dict)
