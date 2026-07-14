from pathlib import Path

class ProjectScanner:

    def scan(self, root: str):
        root = Path(root)

        return {
            "name": root.name,
            "pyproject": (root / "pyproject.toml").exists(),
            "git": (root / ".git").exists(),
        }

project_scanner = ProjectScanner()
