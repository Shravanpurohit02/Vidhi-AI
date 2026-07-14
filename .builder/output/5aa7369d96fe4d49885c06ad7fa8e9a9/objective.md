
BUILDER SPRINT-02
Production Audit Engine

Context

The Builder must support mature production repositories.

The target repository (Vidhi AI) is assumed to be more than 95% production-ready.

Builder must operate in engineering audit mode instead of code generation mode.

Requirements

Analyze the complete repository.

Identify every production subsystem.

Inspect all Python packages and project modules.

Build a repository inventory.

Build a dependency graph.

Detect integration boundaries.

Detect missing production implementations.

Detect duplicate implementations.

Detect placeholder implementations.

Detect TODOs.

Detect pass statements.

Detect incomplete interfaces.

Detect missing tests.

Detect security risks.

Detect performance risks.

Detect architecture violations.

Classify every component using:

- Production Complete
- Production Complete With Minor Improvements
- Missing Production Implementation
- Integration Required
- Security Improvement
- Performance Improvement
- Technical Debt

Generate production engineering artifacts:

.builder/output/<run-id>/engineering_audit.json
.builder/output/<run-id>/architecture_report.json
.builder/output/<run-id>/dependency_report.json
.builder/output/<run-id>/security_report.json
.builder/output/<run-id>/performance_report.json
.builder/output/<run-id>/risk_report.json
.builder/output/<run-id>/release_readiness.json

Review Queue

Generate review tasks only for verified findings.

Do not generate duplicate review tasks.

Merge duplicate findings using:

(target, issue)

as the unique key.

Implementation Rules

Reuse all existing Builder architecture.

Do not redesign existing subsystems.

Do not rewrite working code.

Implement only missing production functionality.

Preserve backward compatibility.

Do not automatically apply patches.

Return production-ready implementation only.
