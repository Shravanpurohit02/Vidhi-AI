import os

DEFAULT_PROVIDER = os.getenv(
    "DEFAULT_LLM_PROVIDER",
    "mock",
).lower()
