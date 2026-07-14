from __future__ import annotations

from app.agents.orchestration.task_classifier import TaskClassifier
from app.agents.orchestration.agent_selector import AgentSelector


class WorkflowEngine:

    def __init__(self):
        self.classifier=TaskClassifier()
        self.selector=AgentSelector()

    def route(self,query:str):

        task=self.classifier.classify(query)

        return {
            "task":task,
            "agent":self.selector.select(task),
        }
