from builder.providers.base import BaseProvider
from builder.providers.response import ProviderResponse

class MockProvider(BaseProvider):

    name = "mock"

    def generate(self, request):
        return ProviderResponse(
            success=True,
            content=f"Executed: {request.prompt}",
            provider=self.name,
        )
