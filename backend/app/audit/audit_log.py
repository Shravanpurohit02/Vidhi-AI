from datetime import UTC, datetime


class AuditLog:

    def __init__(self):
        self.events = []

    def write(self, action: str, actor: str = "system"):
        self.events.append(
            {
                "timestamp": datetime.now(UTC).isoformat(),
                "actor": actor,
                "action": action,
            }
        )

    def all(self):
        return self.events


audit_log = AuditLog()
