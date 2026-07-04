from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorkflowStep:
    name: str
    status: str = "pending"
    result: dict[str, Any] = field(default_factory=dict)


class CourtWorkflow:

    def __init__(self):
        self.steps = []

    def add_step(self, name: str):
        self.steps.append(WorkflowStep(name=name))

    def complete(self, name: str, result: dict[str, Any] | None = None):
        for step in self.steps:
            if step.name == name:
                step.status = "completed"
                step.result = result or {}
                break

    def fail(self, name: str, reason: str):
        for step in self.steps:
            if step.name == name:
                step.status = "failed"
                step.result = {"reason": reason}
                break

    def summary(self):
        return [
            {
                "step": s.name,
                "status": s.status,
                "result": s.result,
            }
            for s in self.steps
        ]
