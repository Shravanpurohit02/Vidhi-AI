from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentSession:
    user_id: int
    history: list[dict[str, Any]] = field(default_factory=list)

    def remember(self, role: str, content: str):
        self.history.append(
            {
                "role": role,
                "content": content,
            }
        )
