from sqlalchemy.orm import Session

from app.services.case_service import CaseService


class CaseWorkspace:

    def __init__(self, db: Session):
        self.db = db

    def create(self, data: dict):
        return CaseService.create_case(
            self.db,
            data,
        )

    def list(self):
        return CaseService.list_cases(
            self.db,
        )

    def get(self, case_id: int):
        return CaseService.get_case(
            self.db,
            case_id,
        )

    def update(
        self,
        case_id: int,
        data: dict,
    ):
        return CaseService.update_case(
            self.db,
            case_id,
            data,
        )

    def delete(
        self,
        case_id: int,
    ):
        return CaseService.delete_case(
            self.db,
            case_id,
        )

    def import_case(
        self,
        court_case: dict,
    ):
        """
        Converts an external court case into a Vidhi AI case.
        This will later map CourtCase -> Case model.
        """
        return {
            "status": "pending",
            "message": "Court import pipeline not implemented.",
            "court_case": court_case,
        }

    def synchronize(
        self,
        case_id: int,
    ):
        return {
            "status": "pending",
            "message": "Synchronization not implemented.",
            "case_id": case_id,
        }
