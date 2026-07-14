import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".builder"))

from builder.planning import (
    analyzer,
    scheduler,
    executor,
)

plan = analyzer.analyze(
    "Full Planning System Verification",
    str(ROOT),
)

queue = scheduler.schedule(plan)

scheduled = 0

while scheduler.next(queue):
    scheduled += 1

result = executor.execute(plan)

assert scheduled == result.total
assert result.completed == result.total
assert result.failed == 0

print("=" * 60)
print("PLANNING SUBSYSTEM VERIFIED")
print("=" * 60)
print("MILESTONES :", len(plan.milestones))
print("TASKS      :", result.total)
print("SCHEDULED  :", scheduled)
print("COMPLETED  :", result.completed)
print("FAILED     :", result.failed)
print("=" * 60)
print("B-02 COMPLETE")
