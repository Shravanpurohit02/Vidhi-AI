from app.schemas.case import CaseCreate, CaseUpdate


def test_case_create_schema():
    case = CaseCreate(
        title="Demo",
        description="Demo",
        court="Supreme Court",
        case_number="CASE-001",
    )

    assert case.title == "Demo"


def test_case_update_schema():
    case = CaseUpdate(
        title="Updated",
        description="Updated",
        court="High Court",
        status="Open",
    )

    assert case.status == "Open"
