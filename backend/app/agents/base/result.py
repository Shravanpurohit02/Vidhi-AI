from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentResult:
    success: bool

    message: str

    answer: str = ""

    sources: list[dict[str, Any]] = field(
        default_factory=list,
    )

    tool_calls: list[dict[str, Any]] = field(
        default_factory=list,
    )

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    data: dict[str, Any] = field(
        default_factory=dict,
    )
