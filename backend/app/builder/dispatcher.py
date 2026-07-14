from dataclasses import dataclass
from typing import Any

from .inspection.engine import engine as inspection_engine
from . import providers  # noqa: F401

from builder.orchestrator.engine import engine as orchestrator_engine
from builder.context.engine import engine as context_engine
from builder.autonomous.engine import engine as autonomous_engine
from builder.validation.engine import engine as validation_engine
from builder.testing.engine import engine as testing_engine
from builder.deployment.engine import engine as deployment_engine


@dataclass(slots=True)
class BuilderRequest:
    operation: str
    workspace: str
    payload: dict[str, Any] | None = None


@dataclass(slots=True)
class BuilderResponse:
    success: bool
    operation: str
    result: Any = None
    error: str | None = None


@dataclass(slots=True)
class OrchestratorRequest:
    workspace: str
    objective: str
    model: str = "default"


class BuilderDispatcher:

    def dispatch(self, request: BuilderRequest) -> BuilderResponse:

        payload = request.payload or {}

        try:
            op = request.operation.lower()

            if op == "inspect":
                result = inspection_engine.inspect(request.workspace)

            elif op == "context":
                result = context_engine.create(
                    request.workspace,
                    payload.get("objective", ""),
                    payload.get("target_file"),
                )

            elif op == "orchestrate":
                orch_request = OrchestratorRequest(
                    workspace=request.workspace,
                    objective=payload.get("objective", ""),
                    model=payload.get("model"),
                )
                result = orchestrator_engine.run(orch_request)

            elif op == "autonomous":
                ctx = dict(payload)
                objective = ctx.pop("objective", "")
                result = autonomous_engine.execute(
                    objective,
                    **ctx,
                )

            elif op == "validate":
                result = validation_engine.validate(request.workspace)

            elif op == "test":
                result = testing_engine.execute(request.workspace)

            elif op == "deploy":
                result = deployment_engine.package(request.workspace)

            else:
                return BuilderResponse(
                    success=False,
                    operation=op,
                    error=f"Unknown operation: {op}",
                )

            return BuilderResponse(
                success=True,
                operation=op,
                result=result,
            )

        except Exception as exc:
            return BuilderResponse(
                success=False,
                operation=request.operation,
                error=str(exc),
            )


dispatcher = BuilderDispatcher()
