import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".builder"))

from builder.planning import analyzer, executor

plan = analyzer.analyze(
    "Execute Builder Plan",
    str(ROOT),
)

result = executor.execute(plan)

print("=" * 60)
print("TOTAL     :", result.total)
print("COMPLETED :", result.completed)
print("FAILED    :", result.failed)
print("EXECUTED  :", len(result.executed))
print("=" * 60)

assert result.total == result.completed
assert result.failed == 0
assert len(result.executed) == result.total
