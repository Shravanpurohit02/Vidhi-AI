# Modified generate_b01_1.py for Test Selective Repair

#!/usr/bin/env python3
from pathlib import Path
import textwrap

ROOT = Path.cwd()
BUILDER = ROOT / ".builder" / "builder"
ENGINEERING = BUILDER / "engineering"
CHANGESET = ENGINEERING / "changeset"

# Updated FILES dictionary with selective repair modifications
FILES = {
    ENGINEERING / "__init__.py": ''' 
    """ 
    Engineering subsystem with selective repair capability.
    """ 
    from .changeset.engine import engine
    from .changeset.repair import repair_service
    __all__ = ["engine", "repair_service"]
    ''',
    CHANGESET / "__init__.py": ''' 
    from .engine import engine
    from .models import (
        EngineeringChangeSet, 
        ChangeFile, 
    )
    from .repair import repair_service
    __all__ = [ 
        "engine", 
        "EngineeringChangeSet", 
        "ChangeFile",
        "repair_service"
    ]
    ''',
    CHANGESET / "models.py": ''' 
    from dataclasses import dataclass, field
    from datetime import datetime
    from uuid import uuid4
    
    @dataclass(slots=True)
    class ChangeFile:
        path: str
        action: str
        reason: str = ""
        
    @dataclass(slots=True)
    class EngineeringChangeSet:
        id: str = field(default_factory=lambda: uuid4().hex)
        created_at: str = field(
            default_factory=lambda: datetime.utcnow().isoformat()
        )
        objective: str = ""
        status: str = "draft"
        files: list[ChangeFile] = field(default_factory=list)
        validation: list[str] = field(default_factory=list)
        risks: list[str] = field(default_factory=list)
        rollback: list[str] = field(default_factory=list)
        metadata: dict = field(default_factory=dict)
        # Added repair_status for tracking
        repair_status: str = "pending"
    ''',
    CHANGESET / "serializer.py": ''' 
    from dataclasses import asdict
    import json
    
    class Serializer:
        def dumps(self, obj):
            return json.dumps(
                asdict(obj), 
                indent=2, 
            )
    serializer = Serializer()
    ''',
    CHANGESET / "storage.py": ''' 
    import json
    from pathlib import Path
    
    STATE = (
        Path.cwd() / ".builder" / "state" / "changesets"
    )
    
    class Storage:
        def save(self, changeset):
            STATE.mkdir(
                parents=True, 
                exist_ok=True, 
            )
            target = STATE / f"{changeset.id}.json"
            target.write_text(
                json.dumps(
                    changeset, 
                    indent=2, 
                ),
                encoding="utf-8",
            )
            return target
    storage = Storage()
    ''',
    CHANGESET / "engine.py": ''' 
    from dataclasses import asdict
    from .models import EngineeringChangeSet
    from .storage import storage
    
    class EngineeringEngine:
        def create(
            self, 
            objective: str, 
        ):
            ecs = EngineeringChangeSet(
                objective=objective,
            )
            storage.save(ecs)
            return ecs
    engine = EngineeringEngine()
    ''',
    # New file for repair service
    CHANGESET / "repair.py": ''' 
    from .models import EngineeringChangeSet
    from .storage import storage
    
    class RepairService:
        def __init__(self, changeset_id: str):
            self.changeset_id = changeset_id
            
        def initiate_repair(self):
            # Logic for initiating repair
            # For demonstration, simply update repair_status
            changeset = self.load_changeset()
            if changeset:
                changeset.repair_status = "in_progress"
                storage.save(changeset)
                return True
            return False
            
        def load_changeset(self) -> EngineeringChangeSet | None:
            try:
                target = storage.STATE / f"{self.changeset_id}.json"
                data = target.read_text(encoding="utf-8")
                # Simplified for demo; in production, use a proper JSON to dataclass converter
                changeset_data = json.loads(data)
                changeset = EngineeringChangeSet(**changeset_data)
                return changeset
            except (FileNotFoundError, json.JSONDecodeError):
                return None
            
        def complete_repair(self, success: bool):
            changeset = self.load_changeset()
            if changeset:
                changeset.repair_status = "success" if success else "failed"
                storage.save(changeset)
                return True
            return False
            
    def repair_service(changeset_id: str):
        return RepairService(changeset_id)
    ''',
}

def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        textwrap.dedent(content).strip() + "\n",
        encoding="utf-8",
    )
    print("CREATED/UPDATED", path.relative_to(ROOT))

def main():
    for path, content in FILES.items():
        write(path, content)
    print()
    print("=" * 60)
    print("B-01.1 SELECTIVE REPAIR UPDATE COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()