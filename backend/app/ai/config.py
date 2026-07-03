from enum import Enum


class AIProvider(str, Enum):
    MOCK = "mock"
    OPENAI = "openai"
    OLLAMA = "ollama"
    GEMINI = "gemini"
    ANTHROPIC = "anthropic"


DEFAULT_PROVIDER = AIProvider.MOCK
