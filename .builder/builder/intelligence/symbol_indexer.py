import ast
from pathlib import Path

from .symbols import (
    Symbol,
    SymbolIndex,
)


class SymbolIndexer:

    def build(
        self,
        workspace:str,
    ):

        index=SymbolIndex()

        root=Path(workspace)

        for file in root.rglob("*.py"):

            try:
                tree=ast.parse(
                    file.read_text(
                        encoding="utf-8",
                        errors="ignore",
                    )
                )

            except Exception:
                continue

            module=".".join(
                file.relative_to(root).with_suffix("").parts
            )

            index.modules[module]=str(file)

            for node in ast.walk(tree):

                if isinstance(
                    node,
                    (
                        ast.ClassDef,
                        ast.FunctionDef,
                        ast.AsyncFunctionDef,
                    ),
                ):

                    kind=type(node).__name__.replace(
                        "Def",
                        "",
                    ).lower()

                    index.symbols.append(
                        Symbol(
                            name=node.name,
                            kind=kind,
                            module=module,
                            line=node.lineno,
                        )
                    )

        return index


indexer=SymbolIndexer()
