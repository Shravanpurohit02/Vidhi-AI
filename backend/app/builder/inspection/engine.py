from dataclasses import asdict
from pathlib import Path
import json

from builder.project import analyzer, indexer
from builder.ast import engine as ast_engine
from builder.dependency import engine as dependency_engine
from builder.repository.index import indexer as repository_indexer
from builder.project_graph.indexer import indexer as project_graph_indexer
from builder.knowledge import engine as knowledge_engine

from .filter import filter
from .report import InspectionReport

SOURCE_ROOTS = (
    "backend",
    "frontend",
    "docs",
    "deployments",
    "scripts",
)

class ProjectInspectionEngine:

    def inspect(self, workspace: str):

        root = Path(workspace)

        report = InspectionReport(
            project=root.name,
            workspace=str(root),
        )

        total_files = 0
        python_files = 0
        json_files = 0
        markdown_files = 0

        for source in SOURCE_ROOTS:

            source_path = root / source

            if not source_path.exists():
                continue

            repository_indexer.build(str(source_path))

            indexer.build(str(source_path))

            repository_indexer.build(str(source_path))

            ast = ast_engine.build(str(source_path))

            deps = dependency_engine.analyze(str(source_path))

            nodes, edges = project_graph_indexer.build(str(source_path))

            indexed = knowledge_engine.build(str(source_path))

            summary = analyzer.summary()

            total_files += summary["files"]
            python_files += summary["python"]
            json_files += summary["json"]
            markdown_files += summary["markdown"]

            report.ast["modules"] = report.ast.get("modules", 0) + len(ast["modules"])
            report.ast["imports"] = report.ast.get("imports", 0) + len(ast["imports"])

            report.dependencies["count"] = report.dependencies.get("count", 0) + len(deps["packages"])

            report.graph["nodes"] = report.graph.get("nodes", 0) + nodes
            report.graph["edges"] = report.graph.get("edges", 0) + edges

            report.knowledge["indexed"] = report.knowledge.get("indexed", 0) + indexed

        report.project_summary = {
            "files": total_files,
            "python": python_files,
            "json": json_files,
            "markdown": markdown_files,
        }

        output = root / ".builder" / "reports"
        output.mkdir(parents=True, exist_ok=True)

        (output / "project_inspection.json").write_text(
            json.dumps(asdict(report), indent=2),
            encoding="utf-8",
        )

        return report

engine = ProjectInspectionEngine()
