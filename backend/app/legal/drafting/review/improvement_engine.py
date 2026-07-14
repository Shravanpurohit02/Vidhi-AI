from __future__ import annotations


class ImprovementEngine:

    def improve(
        self,
        draft: str,
        suggestions: list[str],
    ) -> str:

        if not suggestions:
            return draft

        improvements = "\n".join(f"- {item}" for item in suggestions)

        return draft + "\n\nSuggested Improvements\n" + improvements
