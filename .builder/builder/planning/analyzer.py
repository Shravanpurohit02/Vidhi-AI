from pathlib import Path

from builder.intelligence.impact import impact

from .engine import engine


class PlanAnalyzer:

    def _target(self, objective: str):

        words = [
            w.strip(".,()[]{}")
            for w in objective.split()
        ]

        for word in reversed(words):

            if len(word) > 2:
                return word

        return objective

    def analyze(
        self,
        objective: str,
        workspace: str,
    ):

        plan = engine.create(objective)

        milestone = plan.milestones[0]
        job = milestone.jobs[0]

        report = impact.analyze(
            workspace,
            self._target(objective),
        )

        plan.impact = report

        if report.validation_scope:

            for module in report.validation_scope:

                parts = [p for p in module.split(".") if p]

                filename = "/".join(parts) + ".py"

                engine.add_task(
                    job,
                    title=filename,
                    objective="Inspect " + filename,
                )

            return plan

        root = Path(workspace)

        for file in root.rglob("*.py"):

            engine.add_task(
                job,
                title=file.relative_to(root).as_posix(),
                objective="Inspect " + file.name,
            )

        return plan


analyzer = PlanAnalyzer()
