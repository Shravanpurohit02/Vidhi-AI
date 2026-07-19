import ast
from pathlib import Path


class ReferenceIndex:

    IGNORE = {
        ".git",
        ".builder",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        "node_modules",
        "dist",
        "build",
        "venv",
        ".venv",
    }

    def _ignored(self, path: Path):
        return any(part in self.IGNORE for part in path.parts)

    def build(self, workspace: str):

        workspace = Path(workspace).resolve()

        references = []

        for file in workspace.rglob("*.py"):

            if self._ignored(file):
                continue

            try:
                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                tree = ast.parse(source)

            except Exception:
                continue

            module = file.relative_to(workspace).with_suffix("").as_posix().replace("/", ".")

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):

                    for alias in node.names:

                        references.append({
                            "module": module,
                            "symbol": alias.name.split(".")[0],
                            "kind": "import",
                            "line": getattr(node, "lineno", 0),
                        })

                elif isinstance(node, ast.ImportFrom):

                    if node.module:

                        references.append({
                            "module": module,
                            "symbol": node.module.split(".")[0],
                            "kind": "importfrom",
                            "line": getattr(node, "lineno", 0),
                        })

                    for alias in node.names:

                        references.append({
                            "module": module,
                            "symbol": alias.name,
                            "kind": "importname",
                            "line": getattr(node, "lineno", 0),
                        })

                elif isinstance(node, ast.Call):

                    func = node.func

                    if isinstance(func, ast.Name):

                        references.append({
                            "module": module,
                            "symbol": func.id,
                            "kind": "call",
                            "line": getattr(node, "lineno", 0),
                        })

                    elif isinstance(func, ast.Attribute):

                        references.append({
                            "module": module,
                            "symbol": func.attr,
                            "kind": "call",
                            "line": getattr(node, "lineno", 0),
                        })

                elif isinstance(node, ast.Attribute):

                    references.append({
                        "module": module,
                        "symbol": node.attr,
                        "kind": "attribute",
                        "line": getattr(node, "lineno", 0),
                    })

                elif isinstance(node, ast.Name):

                    references.append({
                        "module": module,
                        "symbol": node.id,
                        "kind": "name",
                        "line": getattr(node, "lineno", 0),
                    })

        return references


reference_index = ReferenceIndex()
indexer = reference_index
