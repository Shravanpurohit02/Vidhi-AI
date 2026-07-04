from datetime import datetime
from typing import Any


class ActivityService:

    def __init__(self):
        self._activities: list[dict[str, Any]] = []

    def log(
        self,
        *,
        event: str,
        user_id: int | None = None,
        entity: str = "",
        entity_id: int | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:

        activity = {
            "timestamp": datetime.utcnow().isoformat(),
            "event": event,
            "user_id": user_id,
            "entity": entity,
            "entity_id": entity_id,
            "metadata": metadata or {},
        }

        self._activities.append(activity)

        return activity

    def recent(self, limit: int = 20):
        return self._activities[-limit:][::-1]
