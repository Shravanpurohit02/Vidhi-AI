from builder.reflection import semantic_engine
from builder.reflection.navigator import navigator

from builder.intelligence.models import (
    ImpactModule,
    ImpactReport,
    ImpactSymbol,
)


class ImpactAnalyzer:

    def analyze(
        self,
        workspace: str,
        target: str,
    ):

        repo = semantic_engine.build(workspace)

        report = ImpactReport(
            target=target,
        )

        for symbol in navigator.symbol(repo, target):

            report.symbols.append(
                ImpactSymbol(
                    name=symbol.name,
                    module=symbol.module,
                    kind=symbol.kind,
                )
            )

        report.references = navigator.references(
            repo,
            target,
        )

        affected = set()

        for ref in report.references:
            affected.add(ref["module"])

        for module in sorted(affected):

            report.modules.append(
                ImpactModule(
                    name=module,
                )
            )

        report.validation_scope = sorted(affected)

        if len(affected) > 25:
            report.risk = "high"
        elif len(affected) > 5:
            report.risk = "medium"
        else:
            report.risk = "low"

        return report


impact = ImpactAnalyzer()
