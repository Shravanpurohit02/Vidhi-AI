from dataclasses import dataclass, field

@dataclass(slots=True)
class InspectionReport:

    project:str=""
    workspace:str=""

    project_summary:dict=field(default_factory=dict)
    repository:dict=field(default_factory=dict)
    ast:dict=field(default_factory=dict)
    dependencies:dict=field(default_factory=dict)
    graph:dict=field(default_factory=dict)
    knowledge:dict=field(default_factory=dict)
    validation:dict=field(default_factory=dict)
    testing:dict=field(default_factory=dict)
