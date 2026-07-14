import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(ROOT / ".builder"))

from builder.intelligence.symbol_indexer import indexer
from builder.intelligence.query import query

idx = indexer.build(str(ROOT))

print("=" * 60)
print("MODULES   :", len(idx.modules))
print("SYMBOLS   :", len(idx.symbols))
print("FUNCTIONS :", len(query.functions(idx)))
print("CLASSES   :", len(query.classes(idx)))
print("=" * 60)

assert len(idx.modules) > 0
assert len(idx.symbols) > 0
