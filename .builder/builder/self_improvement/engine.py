from builder.self_improvement.analyzer import analyzer
from builder.self_improvement.planner import planner

class SelfImprovementEngine:

    def inspect(self, workspace: str):

        issues = analyzer.analyze(workspace)

        return planner.build(issues)

engine = SelfImprovementEngine()
