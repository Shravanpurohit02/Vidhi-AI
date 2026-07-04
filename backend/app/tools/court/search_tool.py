from app.integrations.courts.ecourts import ECourtsProvider
from app.tools.base.result import ToolResult
from app.tools.base.tool import BaseTool


class CourtSearchTool(BaseTool):

    name = "court_search"
    description = "Search official court providers."

    def __init__(self):
        self.provider = ECourtsProvider()

    async def execute(self, **kwargs) -> ToolResult:

        if "cnr" in kwargs:
            result = await self.provider.search_by_cnr(kwargs["cnr"])
        else:
            result = await self.provider.search_case(**kwargs)

        return ToolResult(
            success=True,
            message="Court search executed.",
            data=result,
        )
