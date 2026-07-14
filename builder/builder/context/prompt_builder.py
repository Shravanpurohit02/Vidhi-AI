class PromptBuilder:

    MAX_MODULES = 30

    def build(
        self,
        objective,
        project,
        modules,
        file=None,
    ):

        module_lines = []

        for m in modules[:self.MAX_MODULES]:
            module_lines.append(f"- {m.path}")

        parts = [
            "You are Vidhi Builder.",
            "",
            "Repository Context",
            "==================",
            "",
            "Project Summary:",
            str(project),
            "",
            f"Relevant Modules: {len(modules)}",
            "",
            "Primary Modules",
            "===============",
            *module_lines,
        ]

        if file:
            parts.extend([
                "",
                "Target File",
                "===========",
                f"Path: {file['path']}",
                f"Name: {file['name']}",
                f"Extension: {file['suffix']}",
                f"Lines: {file['lines']}",
                "",
                "Source Code",
                "===========",
                file["source"],
            ])

        parts.extend([
            "",
            "Engineering Objective",
            "=====================",
            objective,
            "",
            "Requirements",
            "============",
            "- Modify only the relevant modules.",
            "- Preserve the existing architecture.",
            "- Reuse existing services before creating new ones.",
            "- Do not duplicate functionality.",
            "- Return production-ready code only.",
        ])

        return "\n".join(parts)


builder = PromptBuilder()
