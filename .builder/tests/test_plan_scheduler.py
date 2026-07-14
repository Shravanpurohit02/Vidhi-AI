import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(ROOT / ".builder"))

from builder.planning import (
    analyzer,
    scheduler,
)

plan = analyzer.analyze(
    "Scheduling Test",
    str(ROOT),
)

queue = scheduler.schedule(plan)

count = 0

while True:

    task = scheduler.next(queue)

    if task is None:
        break

    count += 1

print("=" * 60)
print("TASKS SCHEDULED :", count)
print("=" * 60)

assert count > 0
