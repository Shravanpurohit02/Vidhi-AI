from dataclasses import dataclass, field


@dataclass(slots=True)
class EngineeringState:

    active_changeset: str = ""

    completed_changesets: list[str] = field(default_factory=list)

    failed_changesets: list[str] = field(default_factory=list)

    current_objective: str = ""

    metadata: dict = field(default_factory=dict)
