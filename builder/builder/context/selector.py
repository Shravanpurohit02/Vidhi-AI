from pathlib import Path

from builder.ast import engine


class ContextSelector:

    MAX_FILES = 10

    IGNORE = {
        ".builder",
        ".git",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        "node_modules",
        "dist",
        "build",
    }

    def _ignored(self, path):
        return any(
            part in self.IGNORE
            for part in Path(path).parts
        )

    def _keyword_score(self, module, objective):

        objective = objective.lower()

        score = 0

        values = [
            module.path,
            *module.classes,
            *module.functions,
            *module.async_functions,
            *module.imports,
            *module.global_variables,
        ]

        for value in values:
            value = str(value).lower()

            if value and value in objective:
                score += 10

        if Path(module.path).stem.lower() in objective:
            score += 25

        return score

    def _dependency_score(self, graph, module):

        score = 0

        reverse = graph["reverse"].get(
            module.path,
            [],
        )

        score += len(reverse) * 5

        score += graph["depth"].get(
            module.path,
            0,
        )

        return score

    def select(self, workspace, objective):

        ast = engine.build(workspace)

        modules = [
            m
            for m in ast["modules"]
            if not self._ignored(m.path)
        ]

        graph = ast["imports"]

        ranked = sorted(
            modules,
            key=lambda m:
                self._keyword_score(
                    m,
                    objective,
                )
                +
                self._dependency_score(
                    graph,
                    m,
                ),
            reverse=True,
        )

        ranked = [
            m
            for m in ranked
            if (
                self._keyword_score(
                    m,
                    objective,
                )
                +
                self._dependency_score(
                    graph,
                    m,
                )
            ) > 0
        ]

        if not ranked:
            ranked = modules[:self.MAX_FILES]

        return ranked[:self.MAX_FILES]


selector = ContextSelector()
