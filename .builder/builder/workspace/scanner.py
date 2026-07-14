from pathlib import Path
from dataclasses import dataclass
from fnmatch import fnmatch

@dataclass
class WorkspaceFile:
    path: str
    name: str
    extension: str
    size: int

class WorkspaceScanner:

    def __init__(self):
        self.ignore = self._load_ignore()

    def _load_ignore(self):
        file = Path(".builder/.builderignore")
        if not file.exists():
            return []

        return [
            line.strip()
            for line in file.read_text().splitlines()
            if line.strip() and not line.startswith("#")
        ]

    def _ignored(self, path: Path):
        text = path.as_posix()

        for pattern in self.ignore:
            p = pattern.rstrip("/")

            if fnmatch(text, pattern):
                return True

            if f"/{p}/" in f"/{text}/":
                return True

            if text.startswith(p):
                return True

        return False

    def scan(self, root: str):
        files = []

        for path in Path(root).rglob("*"):

            if self._ignored(path):
                continue

            if not path.is_file():
                continue

            files.append(
                WorkspaceFile(
                    path=str(path),
                    name=path.name,
                    extension=path.suffix,
                    size=path.stat().st_size,
                )
            )

        return files

scanner = WorkspaceScanner()
