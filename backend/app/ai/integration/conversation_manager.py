from __future__ import annotations

from app.ai.integration.memory_manager import MemoryManager


class ConversationManager:

    def __init__(self):
        self.memory = MemoryManager()

    def add_user(
        self,
        conversation_id: str,
        message: str,
    ):
        self.memory.append(
            conversation_id,
            "user",
            message,
        )

    def add_assistant(
        self,
        conversation_id: str,
        message: str,
    ):
        self.memory.append(
            conversation_id,
            "assistant",
            message,
        )

    def history(
        self,
        conversation_id: str,
    ):
        return self.memory.history(conversation_id)

    def clear(
        self,
        conversation_id: str,
    ):
        self.memory.clear(conversation_id)
