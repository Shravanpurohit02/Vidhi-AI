from pathlib import Path

from builder.ast import engine as ast_engine
from builder.codegen import (
    CodeGenerationRequest,
    engine as codegen,
)
from builder.dependency import engine as dependency
from builder.engineering.changeset import engine as ecs
from builder.project import analyzer, indexer

from .context import BuildContext


class Orchestrator:

    def execute(self, request):

        workspace = Path(request.workspace)

        indexer.build(str(workspace))

        ast_data = ast_engine.build(str(workspace))

        deps = dependency.analyze(str(workspace))

        summary = analyzer.summary()

        context = BuildContext(
            project=workspace.name,
            files=summary["files"],
            modules=len(ast_data["modules"]),
            dependencies=len(deps["packages"]),
        )

        changeset = ecs.create(
            objective=request.objective,
            workspace=str(workspace),
        )

        result = codegen.generate(
            CodeGenerationRequest(
                instruction=request.objective,
                context=str(context),
                model=request.model,
            )
        )

        ecs.report(
            changeset,
            summary="Initial engineering generation completed.",
            recommendations=[
                "Validate generated code",
                "Review engineering change set",
            ],
        )

        ecs.save(changeset)

        return {
            "changeset": changeset,
            "generation": result,
        }


orchestrator = Orchestrator()
