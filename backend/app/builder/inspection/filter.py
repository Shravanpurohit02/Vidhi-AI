from pathlib import Path

EXCLUDED_DIRECTORIES = {
    ".git",
    ".builder",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "dist",
    "build",
    ".idea",
    ".vscode",
    ".coverage",
}

EXCLUDED_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".log",
    ".tmp",
    ".bak",
}

class ProjectFilter:

    def include(self, path: Path) -> bool:

        parts = set(path.parts)

        if parts & EXCLUDED_DIRECTORIES:
            return False

        if path.suffix.lower() in EXCLUDED_SUFFIXES:
            return False

        return True

filter = ProjectFilter()
