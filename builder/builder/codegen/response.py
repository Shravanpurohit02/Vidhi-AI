from dataclasses import dataclass

@dataclass(slots=True)
class CodeGenerationResponse:
    success: bool
    provider: str
    model: str
    code: str
    raw: dict
