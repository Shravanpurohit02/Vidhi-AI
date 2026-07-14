from __future__ import annotations

import os


def _env(name: str, default: str = "") -> str:
    return os.getenv(name, default)


DEFAULT_PROVIDER = _env("DEFAULT_PROVIDER", "nvidia")

PROVIDER_PRIORITY = [
    p.strip()
    for p in _env(
        "FALLBACK_PROVIDERS",
        "groq,gemini,openrouter,cerebras,mistral,anthropic,huggingface,ollama,mock",
    ).split(",")
    if p.strip()
]

ROUTING_MODE = _env("ROUTING_MODE", "auto")

ENABLE_PROVIDER_FAILOVER = _env("ENABLE_PROVIDER_FAILOVER", "true").lower() == "true"

ENABLE_PROVIDER_HEALTH_CHECK = (
    _env("ENABLE_PROVIDER_HEALTH_CHECK", "true").lower() == "true"
)

ENABLE_SMART_FALLBACK = _env("ENABLE_SMART_FALLBACK", "true").lower() == "true"

FREE_TIER_ONLY = _env("FREE_TIER_ONLY", "true").lower() == "true"

REQUEST_TIMEOUT = int(_env("REQUEST_TIMEOUT", "60"))

MAX_PROVIDER_RETRIES = int(_env("MAX_PROVIDER_RETRIES", "3"))
