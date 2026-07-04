from app.agents.base.task import AgentTask


class TaskPlanner:

    def create_plan(self, query: str) -> AgentTask:

        q = query.lower()

        if "cnr" in q:
            return AgentTask(
                objective="Search court by CNR",
                steps=[
                    "Extract CNR",
                    "Invoke CourtSearchTool",
                    "Validate response",
                    "Return result",
                ],
            )

        if "import" in q and "case" in q:
            return AgentTask(
                objective="Import case",
                steps=[
                    "Search court",
                    "Preview case",
                    "Create local case",
                    "Link external source",
                ],
            )

        return AgentTask(
            objective="General court request",
            steps=[
                "Determine intent",
                "Select tool",
                "Execute",
            ],
        )
