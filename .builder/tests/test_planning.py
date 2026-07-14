import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/".builder"))

from builder.planning import engine

plan=engine.create("Build Builder")

m=engine.add_milestone(plan,"Phase 2")

j=engine.add_job(m,"Context")

engine.add_task(
    j,
    "Inspect repository",
)

engine.add_task(
    j,
    "Build context",
)

print("="*60)
print("PLAN :",plan.objective)
print("MILESTONES :",len(plan.milestones))
print("TASKS :",len(engine.tasks(plan)))
print("="*60)
