from dataclasses import dataclass, field
from uuid import uuid4


@dataclass(slots=True)
class ProjectFile:

    id: str = field(default_factory=lambda: uuid4().hex)

    path: str = ""
    relative_path: str = ""
    directory: str = ""
    name: str = ""
    extension: str = ""

    category: str = ""

    size: int = 0
    lines: int = 0

    modified: float = 0.0

    sha256: str = ""
