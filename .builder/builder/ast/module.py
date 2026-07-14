from dataclasses import dataclass, field

@dataclass(slots=True)
class Module:
    path: str

    classes: list[str] = field(default_factory=list)
    functions: list[str] = field(default_factory=list)
    async_functions: list[str] = field(default_factory=list)
    imports: list[str] = field(default_factory=list)

    global_variables: list[str] = field(default_factory=list)
    assignments: list[str] = field(default_factory=list)
    decorators: list[str] = field(default_factory=list)
    exports: list[str] = field(default_factory=list)

    docstring: str = ""
    line_count: int = 0
    symbol_count: int = 0
