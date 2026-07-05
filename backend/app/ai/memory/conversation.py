from collections import deque
from typing import Deque


class ConversationMemory:

    def __init__(self, max_messages: int = 20):
        self.messages: Deque[dict[str, str]] = deque(maxlen=max_messages)

    def add(self, role: str, content: str):
        self.messages.append(
            {
                "role": role,
                "content": content,
            }
        )

    def history(self):
        return list(self.messages)

    def clear(self):
        self.messages.clear()
