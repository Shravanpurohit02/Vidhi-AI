from builder.codegen.prompts import SYSTEM_PROMPT
from builder.providers.chat import Message
from builder.providers.execution import ExecutionRequest, engine

class CodeGenerator:

    def generate(self, request):

        execution = ExecutionRequest(
            model=request.model,
            messages=[
                Message(
                    role="system",
                    content=SYSTEM_PROMPT,
                ),
                Message(
                    role="user",
                    content=f"""
Language:
{request.language}

Workspace Context:
{request.context}

Instruction:
{request.instruction}
""".strip(),
                ),
            ],
        )

        return engine.execute(execution)

generator = CodeGenerator()
