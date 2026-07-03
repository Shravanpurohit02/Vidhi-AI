from app.ai.interfaces.base_provider import BaseAIProvider


class MockAIProvider(BaseAIProvider):

    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> str:
        return (
            "Mock AI Response\\n\\n"
            f"Prompt: {prompt}"
        )
