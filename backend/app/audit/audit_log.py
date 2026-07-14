from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

AUDIT_FILE = Path("logs/audit.log")
AUDIT_FILE.parent.mkdir(parents=True, exist_ok=True)


class AuditLog:

    def __init__(self):
        self.events = []

    def write(
        self,
        action: str,
        actor: str = "system",
    ):
        event = {
            "timestamp": datetime.now(UTC).isoformat(),
            "actor": actor,
            "action": action,
        }

        self.events.append(event)

        with AUDIT_FILE.open(
            "a",
            encoding="utf-8",
        ) as f:
            f.write(json.dumps(event) + "\n")

    def all(self):
        return list(self.events)


audit_log = AuditLog()
