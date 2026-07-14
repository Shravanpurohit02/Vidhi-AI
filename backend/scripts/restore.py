from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BACKUPS = ROOT / "backups"

if len(sys.argv) != 2:
    print("Usage: python scripts/restore.py <backup_folder>")
    raise SystemExit(1)

backup = BACKUPS / sys.argv[1]

if not backup.exists():
    print("Backup not found.")
    raise SystemExit(1)

items = [
    "vidhi_ai.db",
    "vector_store.db",
    "storage",
    "logs",
]

for item in items:
    source = backup / item
    destination = ROOT / item

    if not source.exists():
        continue

    if destination.exists():
        if destination.is_dir():
            shutil.rmtree(destination)
        else:
            destination.unlink()

    if source.is_dir():
        shutil.copytree(source, destination)
    else:
        shutil.copy2(source, destination)

print("Restore completed successfully.")
