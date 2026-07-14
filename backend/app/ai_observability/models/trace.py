from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(slots=True)
class AITrace:
    trace_id: str
    feature: str
    provider: str
    model: str

    prompt: str = ""
    response: str = ""

    input_tokens: int = 0
    output_tokens: int = 0

    latency_ms: float = 0.0
    estimated_cost: float = 0.0

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )
