import json
from dataclasses import asdict
from pathlib import Path

from builder.core import runtime

SESSION_FILE = Path(".builder/state/session.json")

def save_session() -> None:
    SESSION_FILE.parent.mkdir(parents=True, exist_ok=True)
    SESSION_FILE.write_text(
        json.dumps(
            {
                "session_id": runtime.session_id,
                "started_at": runtime.started_at.isoformat(),
                "workspace": str(runtime.workspace),
                "environment": runtime.environment,
                "builder_version": runtime.builder_version,
                "project": runtime.project.name,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
