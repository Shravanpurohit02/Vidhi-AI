from app.llm.base import BaseLLM


class MockLLM(BaseLLM):

    provider = "mock"

    async def generate(
        self,
        prompt: str,
        system: str = "",
    ) -> str:

        return (
            "Mock LLM Response\n\n"
            f"System: {system}\n\n"
            f"Prompt: {prompt}"
        )
