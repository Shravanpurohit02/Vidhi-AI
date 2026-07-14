from pathlib import Path
import json

from builder.project import indexer, analyzer
from builder.ast import engine as ast_engine
from builder.dependency import engine as dependency_engine
from builder.graph import indexer as graph_indexer
from builder.repository import indexer as repository_indexer
from builder.validation import engine as validation_engine
from builder.testing import engine as testing_engine
from builder.knowledge import engine as knowledge_engine

ROOT = Path.cwd()

print("=" * 80)
print("VIDHI BUILDER - FULL PROJECT INSPECTION")
print("=" * 80)

print("\n[1/8] Repository Index")
repository_indexer.build(str(ROOT))

print("\n[2/8] Project Index")
indexer.build(str(ROOT))
summary = analyzer.summary()

print("\n[3/8] AST Analysis")
ast = ast_engine.build(str(ROOT))

print("\n[4/8] Dependency Analysis")
deps = dependency_engine.analyze(str(ROOT))

print("\n[5/8] Knowledge Index")
knowledge_engine.build(str(ROOT))

print("\n[6/8] Graph Analysis")
nodes, edges = graph_indexer.build(str(ROOT))

print("\n[7/8] Validation")
validation = validation_engine.validate(str(ROOT))

print("\n[8/8] Test Inspection")
tests = testing_engine.execute(str(ROOT))

report = {
    "project": ROOT.name,
    "workspace": str(ROOT),
    "summary": summary,
    "ast": {
        "modules": len(ast["modules"]),
        "imports": len(ast["imports"]),
    },
    "dependencies": {
        "count": len(deps["packages"]),
        "packages": deps["packages"],
    },
    "graph": {
        "nodes": nodes,
        "edges": edges,
    },
    "validation": validation,
    "tests": tests,
}

report_dir = ROOT / ".builder" / "reports"
report_dir.mkdir(parents=True, exist_ok=True)

report_file = report_dir / "project_inspection.json"

report_file.write_text(
    json.dumps(report, indent=2),
    encoding="utf-8",
)

print("\n")
print("=" * 80)
print("INSPECTION COMPLETE")
print("=" * 80)

print(f"Project      : {ROOT.name}")
print(f"Files        : {summary['files']}")
print(f"Python Files : {summary['python']}")
print(f"Modules      : {len(ast['modules'])}")
print(f"Dependencies : {len(deps['packages'])}")
print(f"Graph Nodes  : {nodes}")
print(f"Graph Edges  : {edges}")
print(f"Validation   : {validation['passed']}/{validation['files']}")
print(f"Tests        : {tests['passed']}/{tests['tests']}")
print(f"\nReport Saved : {report_file}")
