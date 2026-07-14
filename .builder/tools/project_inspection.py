from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[2]

BUILDER_ROOT = ROOT / ".builder"

sys.path.insert(0, str(BUILDER_ROOT))

from builder.project import analyzer, indexer
from builder.ast import engine as ast_engine
from builder.dependency import engine as dependency_engine
from builder.graph import indexer as graph_indexer
from builder.repository import indexer as repository_indexer
from builder.knowledge import engine as knowledge_engine
from builder.validation import engine as validation_engine
from builder.testing import engine as testing_engine

print("=" * 80)
print("VIDHI BUILDER PROJECT INSPECTION")
print("=" * 80)

repository_indexer.build(str(ROOT))

indexer.build(str(ROOT))
summary = analyzer.summary()

ast = ast_engine.build(str(ROOT))
deps = dependency_engine.analyze(str(ROOT))

knowledge_engine.build(str(ROOT))

nodes, edges = graph_indexer.build(str(ROOT))

validation = validation_engine.validate(str(ROOT))
tests = testing_engine.execute(str(ROOT))

report = {
    "summary": summary,
    "modules": len(ast["modules"]),
    "imports": len(ast["imports"]),
    "dependencies": len(deps["packages"]),
    "graph_nodes": nodes,
    "graph_edges": edges,
    "validation": validation,
    "tests": tests,
}

report_dir = ROOT / ".builder" / "reports"
report_dir.mkdir(parents=True, exist_ok=True)

report_path = report_dir / "inspection_report.json"

report_path.write_text(
    json.dumps(report, indent=2),
    encoding="utf-8",
)

print(json.dumps(report, indent=2))
print()
print(report_path)
