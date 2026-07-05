from pathlib import Path

REQUIRED_FILES = [
    "app/models/hearing.py",
    "app/models/task.py",
    "app/models/note.py",
    "app/models/evidence.py",
    "app/models/bookmark.py",
    "app/models/annotation.py",
    "app/models/client.py",
    "app/models/contact_log.py",
    "app/api/v1/workspace.py",
    "app/api/v1/clients.py",
]


def test_workspace_architecture():
    for file in REQUIRED_FILES:
        assert Path(file).exists(), f"{file} missing"
