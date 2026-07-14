from dataclasses import dataclass

from .runtime import PROJECT_ROOT

@dataclass(slots=True)
class BuilderContext:
    project: str
    workspace: str
    backend: str
    frontend: str

def create_context() -> BuilderContext:
    return BuilderContext(
        project="Vidhi-AI",
        workspace=str(PROJECT_ROOT),
        backend=str(PROJECT_ROOT / "backend"),
        frontend=str(PROJECT_ROOT / "frontend"),
    )
