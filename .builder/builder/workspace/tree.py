from pathlib import Path

class WorkspaceTree:

    def build(self, root: str):
        return [
            str(p.relative_to(root))
            for p in sorted(Path(root).rglob("*"))
        ]

tree = WorkspaceTree()
