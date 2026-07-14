from dataclasses import dataclass

@dataclass(slots=True)
class WorkspaceFile:
    path: str
    name: str
    extension: str
    size: int
