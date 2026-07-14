import time

from builder.execution.result import ExecutionResult
from builder.planning import analyzer
from builder.planning.executor import executor as planning_executor
from builder.validation import engine as validation
from builder.testing import engine as testing
from builder.autonomous_runtime.repair import repair
from builder.engineering.changeset import engine as changesets
from builder.output import engine as output


class Executor:

    MAX_REPAIRS = 3

    def execute(self, context):

        started = time.perf_counter()

        result = ExecutionResult()

        changeset = changesets.create(
            objective="Execution",
            workspace=".",
        )

        artifact = output.create(
            objective="Execution",
            workspace=".",
            metadata={
                "changeset": changeset.id,
                "started": started,
            },
        )

        if isinstance(artifact, dict):
            result.artifacts.append(artifact["path"])
        else:
            result.artifacts.extend(artifact.files)
        result.changeset = changeset.id

        try:

            plan = analyzer.analyze(
                objective="Execution",
                workspace=".",
            )

            planning_result = planning_executor.execute(plan)

            result.completed_stages.append("planning")


            repairs = 0

            while True:

                if (
                    hasattr(plan, "impact")
                    and plan.impact
                    and plan.impact.validation_scope
                ):
                    result.validation = validation.validate_files(
                        plan.impact.validation_scope
                    )
                else:
                    result.validation = validation.validate(".")

                result.completed_stages.append("validation")

                if result.validation.get("failed", 0) == 0:
                    break

                if repairs >= self.MAX_REPAIRS:
                    result.failed_stages.append("validation")
                    break

                if (
                    hasattr(plan, "impact")
                    and plan.impact
                    and plan.impact.validation_scope
                ):
                    repair.repair(
                        workspace=".",
                        paths=plan.impact.validation_scope,
                        context={
                            "validation": result.validation,
                            "testing": result.testing,
                        },
                    )
                else:
                    repair.repair(
                        workspace=".",
                        context={
                            "validation": result.validation,
                            "testing": result.testing,
                        },
                    )

                repairs += 1

                result.completed_stages.append(
                    f"repair-{repairs}"
                )

            if (
                hasattr(plan, "impact")
                and plan.impact
                and plan.impact.validation_scope
            ):
                result.testing = testing.execute_files(
                    plan.impact.validation_scope
                )
            else:
                result.testing = testing.execute(".")

            result.completed_stages.append("testing")

            result.success = (
                result.validation.get("failed", 0) == 0
                and
                result.testing.get("failed", 0) == 0
            )

            if result.success:
                changesets.complete(changeset)

            changesets.save(changeset)

        except Exception as exc:

            result.success = False
            result.failed_stages.append(type(exc).__name__)
            result.message = str(exc)

            changesets.report(
                changeset,
                summary=str(exc),
                recommendations=[
                    "Review execution log",
                    "Run repair pipeline",
                ],
            )

            changesets.save(changeset)

        result.elapsed = round(
            time.perf_counter() - started,
            6,
        )

        if result.success and not result.message:
            result.message = "completed"

        return result


executor = Executor()
