from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional
from uuid import uuid4

from builder.models.project import Project

@dataclass(slots=True)
class RuntimeContext:
    session_id: str = field(default_factory=lambda: uuid4().hex)
    started_at: datetime = field(default_factory=datetime.utcnow)
    workspace: Path = field(default_factory=Path.cwd)
    environment: str = "development"
    builder_version: str = "0.1.0-alpha.1"
    project: Optional[Project] = None
