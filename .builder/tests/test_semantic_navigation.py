import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(ROOT / ".builder"))

from builder.reflection.semantic_engine import engine
from builder.reflection.navigator import navigator

repo = engine.build(str(ROOT))

first_module = next(iter(repo.modules))

print("=" * 60)
print("MODULE :", first_module)
print("CALLEES:", len(navigator.callees(repo, first_module)))
print("REFS   :", len(navigator.references(repo, first_module)))
print("=" * 60)

assert navigator.references(repo, first_module) is not None
assert navigator.callees(repo, first_module) is not None
