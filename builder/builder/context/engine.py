from builder.context.file_context import context as files
from builder.context.module_context import context as modules
from builder.context.project_context import context as project
from builder.context.prompt_builder import builder
from builder.context.selector import selector


class ContextEngine:

    def create(
        self,
        workspace: str,
        objective: str,
    ) -> str:

        project_context = project.build(workspace)

        module_context = modules.build(
            workspace,
            objective,
        )

        selected = selector.select(
            workspace,
            objective,
        )

        file_contexts = []

        for module in selected:
            try:
                ctx = files.build(module.path)
                if ctx:
                    file_contexts.append(ctx)
            except Exception:
                pass

        return builder.build(
            objective=objective,
            project=project_context,
            modules=module_context,
            files=file_contexts,
        )


engine = ContextEngine()
