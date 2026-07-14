from dataclasses import dataclass, field


@dataclass(slots=True)
class ExecutionResult:
    total: int = 0
    completed: int = 0
    failed: int = 0
    executed: list[str] = field(default_factory=list)


class PlanExecutor:

    def execute(self, plan):

        result = ExecutionResult()

        for milestone in plan.milestones:
            for job in milestone.jobs:
                for task in job.tasks:

                    task.status = "completed"

                    result.total += 1
                    result.completed += 1
                    result.executed.append(task.title)

        return result


executor = PlanExecutor()
