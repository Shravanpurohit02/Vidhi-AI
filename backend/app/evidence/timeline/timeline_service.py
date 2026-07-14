from __future__ import annotations

from datetime import datetime


class TimelineService:

    def event(
        self,
        actor: str,
        action: str,
        notes: str = "",
    ) -> dict:

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "actor": actor,
            "action": action,
            "notes": notes,
        }
