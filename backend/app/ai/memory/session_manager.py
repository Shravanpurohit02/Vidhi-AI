from __future__ import annotations

import uuid

class SessionManager:

    @staticmethod
    def create()->str:
        return str(uuid.uuid4())
