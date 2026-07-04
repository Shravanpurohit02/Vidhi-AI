from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentResult:
    success: bool
    message: str
    data: dict[str, Any] = field(default_factory=dict)
