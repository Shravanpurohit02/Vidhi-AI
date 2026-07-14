import ast
from pathlib import Path

from builder.reflection.database import database
from builder.reflection.module import Module
from builder.reflection.symbol import Symbol

class ReflectionIndexer:

    def build(self, workspace: str):
        database.modules.clear()
        database.symbols.clear()

        for path in Path(workspace).rglob("*.py"):
            module = Module(
                path=str(path),
                name=path.stem,
            )

            database.modules[module.path] = module

            try:
                tree = ast.parse(path.read_text(encoding="utf-8"))
            except Exception:
                continue

            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    database.symbols.append(
                        Symbol(
                            module=module.path,
                            name=node.name,
                            kind="class",
                        )
                    )
                elif isinstance(node, ast.FunctionDef):
                    database.symbols.append(
                        Symbol(
                            module=module.path,
                            name=node.name,
                            kind="function",
                        )
                    )

        return (
            len(database.modules),
            len(database.symbols),
        )

indexer = ReflectionIndexer()
