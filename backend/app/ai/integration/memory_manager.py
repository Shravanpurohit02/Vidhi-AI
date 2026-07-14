from __future__ import annotations


class MemoryManager:

    def __init__(self):
        self._memory: dict[str, list[dict]] = {}

    def append(
        self,
        conversation_id: str,
        role: str,
        content: str,
    ) -> None:

        self._memory.setdefault(
            conversation_id,
            [],
        ).append(
            {
                "role": role,
                "content": content,
            }
        )

    def history(
        self,
        conversation_id: str,
    ) -> list[dict]:

        return self._memory.get(
            conversation_id,
            [],
        )

    def clear(
        self,
        conversation_id: str,
    ) -> None:

        self._memory.pop(
            conversation_id,
            None,
        )
