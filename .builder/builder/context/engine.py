from builder.context.file_context import context as files
from builder.context.module_context import context as modules
from builder.context.project_context import context as project
from builder.context.prompt_builder import builder


class ContextEngine:

    def create(
        self,
        workspace: str,
        objective: str,
        target_file: str | None = None,
    ) -> str:

        project_context = project.build(workspace)
        module_context = modules.build(workspace, objective)

        file_context = None

        if target_file:
            try:
                file_context = files.build(target_file)
            except Exception:
                file_context = None

        return builder.build(
            objective=objective,
            project=project_context,
            modules=module_context,
            file=file_context,
        )


engine = ContextEngine()
