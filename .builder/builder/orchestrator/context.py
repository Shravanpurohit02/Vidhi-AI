from dataclasses import dataclass

@dataclass(slots=True)
class BuildContext:
    project: str
    files: int
    modules: int
    dependencies: int
