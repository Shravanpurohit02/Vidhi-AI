from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BACKUPS = ROOT / "backups"

if len(sys.argv) != 2:
    print("Usage: python scripts/verify_backup.py <backup_folder>")
    raise SystemExit(1)

backup = BACKUPS / sys.argv[1]

required = [
    "vidhi_ai.db",
    "vector_store.db",
    "storage",
    "logs",
]

missing = []

for item in required:
    if not (backup / item).exists():
        missing.append(item)

if missing:
    print("Missing:")
    for item in missing:
        print(f" - {item}")
    raise SystemExit(1)

print("Backup verified successfully.")
