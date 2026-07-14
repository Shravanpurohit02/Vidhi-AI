from dataclasses import dataclass

@dataclass(slots=True)
class InspectionContext:
    workspace:str
    backend:str
    frontend:str
