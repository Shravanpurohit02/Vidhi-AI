from dataclasses import dataclass, field

@dataclass(slots=True)
class RuntimeManifest:
    modules: int = 0
    classes: int = 0
    functions: int = 0
    files: int = 0
