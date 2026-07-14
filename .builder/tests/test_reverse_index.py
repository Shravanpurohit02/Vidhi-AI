import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".builder"))

from builder.reflection.semantic_engine import engine

repo = engine.build(str(ROOT))

entries = len(repo.reverse_index)

refs = sum(
    len(v)
    for v in repo.reverse_index.values()
)

print("=" * 60)
print("REVERSE SYMBOLS :", entries)
print("TOTAL LINKS     :", refs)
print("=" * 60)

assert entries > 0
assert refs > 0
