import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(ROOT / ".builder"))

from builder.intelligence.dependency_map import dependency_map

graph = dependency_map.build(str(ROOT))

edges = sum(
    len(v)
    for v in graph.values()
)

print("=" * 60)
print("MODULES :", len(graph))
print("IMPORTS :", edges)
print("=" * 60)

assert len(graph) > 0
assert edges > 0
