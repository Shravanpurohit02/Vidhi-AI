import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(ROOT / ".builder"))

from builder.planning import analyzer, engine

plan = analyzer.analyze(
    "Inspect Builder",
    str(ROOT),
)

print("=" * 60)
print("OBJECTIVE :", plan.objective)
print("MILESTONES:", len(plan.milestones))
print("TASKS     :", len(engine.tasks(plan)))
print("=" * 60)
