from builder.codegen.prompts import SYSTEM_PROMPT
from builder.context import engine as context_engine
from builder.providers.chat import Message
from builder.providers.execution import ExecutionRequest, engine


class CodeGenerator:

    def generate(self, request):

        context = context_engine.create(
            workspace=request.workspace,
            objective=request.instruction,
        )

        if request.context:
            context = (
                f"{context}\n\n"
                "Additional Context\n"
                "==================\n"
                f"{request.context}"
            )

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

Workspace:
{request.workspace}

Repository Context:
{context}

Instruction:
{request.instruction}
""".strip(),
                ),
            ],
        )

        return engine.execute(execution)


generator = CodeGenerator()
