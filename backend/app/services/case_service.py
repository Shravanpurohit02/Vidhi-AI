from sqlalchemy.orm import Session

from app.repositories.case_repository import CaseRepository


class CaseService:

    @staticmethod
    def create_case(db: Session, data: dict):
        existing = CaseRepository.get_by_case_number(
            db,
            data["case_number"],
        )

        if existing:
            raise ValueError("Case number already exists")

        return CaseRepository.create(db, data)

    @staticmethod
    def list_cases(db: Session):
        return CaseRepository.list(db)

    @staticmethod
    def get_case(db: Session, case_id: int):
        case = CaseRepository.get_by_id(db, case_id)

        if case is None:
            raise ValueError("Case not found")

        return case

    @staticmethod
    def update_case(db: Session, case_id: int, data: dict):
        case = CaseRepository.get_by_id(db, case_id)

        if case is None:
            raise ValueError("Case not found")

        return CaseRepository.update(db, case, data)

    @staticmethod
    def delete_case(db: Session, case_id: int):
        case = CaseRepository.get_by_id(db, case_id)

        if case is None:
            raise ValueError("Case not found")

        CaseRepository.delete(db, case)

    @staticmethod
    def search_cases(db: Session, query: str):
        return CaseRepository.search(db, query)

    @staticmethod
    def filter_by_status(db: Session, status: str):
        return CaseRepository.get_by_status(db, status)

    @staticmethod
    def get_statistics(db: Session):
        return CaseRepository.get_statistics(db)
