from pathlib import Path

class WorkspaceScanner:

    def scan(self, root: str):
        return [
            str(p)
            for p in Path(root).rglob("*")
            if p.is_file()
        ]

workspace_scanner = WorkspaceScanner()
