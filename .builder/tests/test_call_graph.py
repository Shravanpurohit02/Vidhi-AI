import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(ROOT / ".builder"))

from builder.reflection.call_graph import call_graph

graph = call_graph.build(str(ROOT))

edges = sum(
    len(v)
    for v in graph.values()
)

print("=" * 60)
print("MODULES :", len(graph))
print("CALLS   :", edges)
print("=" * 60)

assert edges > 0
