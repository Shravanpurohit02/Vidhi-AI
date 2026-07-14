from dataclasses import dataclass, field
from pathlib import Path

@dataclass(slots=True)
class Project:
    root: Path
    name: str
    detected: bool
    pyproject: Path | None = None
    git: Path | None = None
    metadata: dict = field(default_factory=dict)
