from pathlib import Path
import hashlib

from builder.repository.database import database
from builder.repository.file import RepositoryFile


class RepositoryIndexer:

    IGNORE_DIRS = {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        "node_modules",
        "dist",
        "build",
    }

    def _category(self, rel: str):

        rel = rel.replace("\\", "/")

        if rel.startswith("backend/"):
            return "backend"
        if rel.startswith("frontend/"):
            return "frontend"
        if rel.startswith(".builder/"):
            return "builder"
        if "/tests/" in rel or rel.startswith("tests/"):
            return "test"
        if "/migrations/" in rel:
            return "migration"
        if rel.endswith((".json", ".yaml", ".yml", ".toml", ".ini")):
            return "config"
        if rel.endswith((".md", ".txt", ".rst")):
            return "documentation"

        return "other"

    def _sha256(self, path: Path):

        h = hashlib.sha256()

        with path.open("rb") as f:
            while True:
                chunk = f.read(65536)
                if not chunk:
                    break
                h.update(chunk)

        return h.hexdigest()

    def build(self, workspace: str):

        root = Path(workspace).resolve()

        total = 0

        for path in root.rglob("*"):

            if any(part in self.IGNORE_DIRS for part in path.parts):
                continue

            if not path.is_file():
                continue

            try:
                lines = len(
                    path.read_text(
                        encoding="utf-8",
                        errors="ignore",
                    ).splitlines()
                )
            except Exception:
                lines = 0

            rel = str(path.relative_to(root))

            database.add(
                RepositoryFile(
                    path=str(path),
                    relative_path=rel,
                    directory=str(path.parent),
                    name=path.name,
                    extension=path.suffix,
                    category=self._category(rel),
                    size=path.stat().st_size,
                    lines=lines,
                    modified=path.stat().st_mtime,
                    sha256=self._sha256(path),
                )
            )

            total += 1

        return total


indexer = RepositoryIndexer()
