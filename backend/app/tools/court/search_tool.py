from app.integrations.courts.ecourts import ECourtsProvider
from app.tools.base.result import ToolResult
from app.tools.base.tool import BaseTool


class CourtSearchTool(BaseTool):

    name = "court_search"
    description = "Search official court providers."

    def __init__(self):
        self.provider = ECourtsProvider()

    async def execute(self, **kwargs) -> ToolResult:

        if kwargs.get("cnr"):
            result = await self.provider.search_by_cnr(
                kwargs["cnr"],
            )

        elif kwargs.get("case_number"):
            result = await self.provider.search_case(
                **kwargs,
            )

        else:
            raise ValueError("Either 'cnr' or 'case_number' must be provided.")

        return ToolResult(
            success=True,
            message="Court search executed.",
            data=result,
        )
