from app.agents.base.task import AgentTask


class TaskPlanner:
    """
    Lightweight task planner for the v1 agent framework.

    Court planning is intentionally excluded.
    It will return in v2 with the Court Agent.
    """

    def create_plan(
        self,
        query: str,
    ) -> AgentTask:

        q = query.lower()

        if any(
            word in q
            for word in (
                "research",
                "precedent",
                "judgment",
                "citation",
                "case law",
            )
        ):
            return AgentTask(
                objective="Legal research",
                steps=[
                    "Route to ResearchAgent",
                    "Execute research",
                    "Return answer",
                ],
            )

        if any(
            word in q
            for word in (
                "reason",
                "reasoning",
                "analyse",
                "analyze",
                "interpret",
                "explain",
            )
        ):
            return AgentTask(
                objective="Legal reasoning",
                steps=[
                    "Route to ReasoningAgent",
                    "Execute reasoning",
                    "Return analysis",
                ],
            )

        if any(
            word in q
            for word in (
                "draft",
                "petition",
                "application",
                "notice",
                "agreement",
                "affidavit",
                "reply",
            )
        ):
            return AgentTask(
                objective="Legal drafting",
                steps=[
                    "Route to DraftingAgent",
                    "Generate draft",
                    "Return document",
                ],
            )

        return AgentTask(
            objective="General AI request",
            steps=[
                "Route request",
                "Execute agent",
                "Return response",
            ],
        )
