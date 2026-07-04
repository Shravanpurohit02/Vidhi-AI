from dataclasses import dataclass, field
from typing import Any

@dataclass
class ToolResult:
    success: bool
    message: str
    data: dict[str, Any] = field(default_factory=dict)
