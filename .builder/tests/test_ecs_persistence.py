import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".builder"))

from builder.engineering.changeset import engine


def main():

    ecs = engine.create(
        objective="Persistence Test",
        workspace=str(ROOT),
    )

    engine.add_file(
        ecs,
        "builder/example.py",
        "create",
        "Persistence verification",
    )

    engine.add_risk(
        ecs,
        "medium",
        "Persistence",
        "Verify ECS serialization",
    )

    engine.report(
        ecs,
        "Persistence verification complete.",
    )

    engine.save(ecs)

    state = (
        ROOT
        / ".builder"
        / "state"
        / "changesets"
        / f"{ecs.id}.json"
    )

    data = json.loads(
        state.read_text(
            encoding="utf-8",
        )
    )

    assert len(data["files"]) == 1
    assert len(data["risks"]) == 1
    assert data["report"]["summary"] == "Persistence verification complete."

    print("=" * 60)
    print("ECS PERSISTENCE VERIFIED")
    print("=" * 60)
    print("CHANGESET :", ecs.id)
    print("FILES     :", len(data["files"]))
    print("RISKS     :", len(data["risks"]))
    print("REPORT    :", data["report"]["summary"])
    print("=" * 60)
    print("B-01 STABILIZATION COMPLETE")


if __name__ == "__main__":
    main()
