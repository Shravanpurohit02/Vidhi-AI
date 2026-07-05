from app.ai.interfaces.base_provider import BaseAIProvider


class MockAIProvider(BaseAIProvider):

    @property
    def name(self) -> str:
        return "mock"

    @property
    def model(self) -> str:
        return "mock-model"

    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:
        return "Mock AI Response\n\n" f"Prompt: {prompt}"
