import ast
from pathlib import Path


class ReferenceIndexer:

    def build(
        self,
        workspace: str,
    ):

        references = {}

        root = Path(workspace)

        for file in root.rglob("*.py"):

            try:
                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                tree = ast.parse(source)

            except Exception:
                continue

            module = ".".join(
                file.relative_to(root).with_suffix("").parts
            )

            for node in ast.walk(tree):

                if isinstance(node, ast.Name):
                    name = node.id

                elif isinstance(node, ast.Attribute):
                    name = node.attr

                else:
                    continue

                references.setdefault(name, []).append(
                    {
                        "module": module,
                        "path": str(file),
                        "line": getattr(node, "lineno", 0),
                    }
                )

        return references


indexer = ReferenceIndexer()
