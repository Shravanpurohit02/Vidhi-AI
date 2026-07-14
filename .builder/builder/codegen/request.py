from dataclasses import dataclass

@dataclass(slots=True)
class CodeGenerationRequest:
    instruction: str
    language: str = "python"
    context: str = ""
    model: str = ""
