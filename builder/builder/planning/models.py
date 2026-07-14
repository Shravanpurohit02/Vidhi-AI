from dataclasses import dataclass, field
from uuid import uuid4

from builder.intelligence.models import ImpactReport


@dataclass(slots=True)
class Task:
    id:str=field(default_factory=lambda:uuid4().hex)
    title:str=""
    objective:str=""
    status:str="pending"


@dataclass(slots=True)
class Job:
    id:str=field(default_factory=lambda:uuid4().hex)
    title:str=""
    tasks:list[Task]=field(default_factory=list)


@dataclass(slots=True)
class Milestone:
    id:str=field(default_factory=lambda:uuid4().hex)
    title:str=""
    jobs:list[Job]=field(default_factory=list)


@dataclass(slots=True)
class EngineeringPlan:
    id:str=field(default_factory=lambda:uuid4().hex)
    objective:str=""
    milestones:list[Milestone]=field(default_factory=list)

    impact: ImpactReport | None = None
