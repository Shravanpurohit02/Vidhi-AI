from app.llm.mock import MockLLM


class LLMService:

    def __init__(self):
        self.providers = {
            "mock": MockLLM(),
        }

        self.default = "mock"

    async def generate(
        self,
        prompt: str,
        system: str = "",
        provider: str | None = None,
    ) -> str:

        provider = provider or self.default

        llm = self.providers[provider]

        return await llm.generate(
            prompt=prompt,
            system=system,
        )
