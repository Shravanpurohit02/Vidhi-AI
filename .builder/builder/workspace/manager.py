from builder.workspace.scanner import scanner
from builder.workspace.tree import tree

class WorkspaceManager:

    def inspect(self, root: str):
        files = scanner.scan(root)

        return {
            "files": len(files),
            "tree": tree.build(root),
        }

manager = WorkspaceManager()
