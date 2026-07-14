from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BACKUPS = ROOT / "backups"
BACKUPS.mkdir(exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

backup_dir = BACKUPS / timestamp
backup_dir.mkdir()

items = [
    "vidhi_ai.db",
    "vector_store.db",
    "storage",
    "logs",
]

for item in items:
    src = ROOT / item

    if not src.exists():
        continue

    dst = backup_dir / src.name

    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)

print(f"Backup created: {backup_dir}")

backups = sorted([d for d in BACKUPS.iterdir() if d.is_dir()])

while len(backups) > 10:
    shutil.rmtree(backups.pop(0))

print(f"Total backups retained: {len(backups)}")
