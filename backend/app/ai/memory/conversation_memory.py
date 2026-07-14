from __future__ import annotations

from collections import defaultdict, deque

class ConversationMemory:

    def __init__(self, max_messages:int=100):
        self.max_messages=max_messages
        self.sessions=defaultdict(lambda:deque(maxlen=self.max_messages))

    def add(self, session_id:str, role:str, content:str):
        self.sessions[session_id].append({
            "role":role,
            "content":content,
        })

    def history(self, session_id:str):
        return list(self.sessions[session_id])

    def clear(self, session_id:str):
        self.sessions.pop(session_id,None)

    def clear_all(self):
        self.sessions.clear()
