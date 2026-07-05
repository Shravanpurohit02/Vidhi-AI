from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.case import Case


class CaseRepository:

    @staticmethod
    def create(db: Session, data: dict) -> Case:
        case = Case(**data)
        db.add(case)
        db.commit()
        db.refresh(case)
        return case

    @staticmethod
    def list(db: Session):
        return db.query(Case).order_by(Case.id.desc()).all()

    @staticmethod
    def get_by_id(db: Session, case_id: int):
        return db.query(Case).filter(Case.id == case_id).first()

    @staticmethod
    def get_by_case_number(db: Session, case_number: str):
        return db.query(Case).filter(Case.case_number == case_number).first()

    @staticmethod
    def search(db: Session, query: str):
        return (
            db.query(Case)
            .filter(
                or_(
                    Case.title.ilike(f"%{query}%"),
                    Case.case_number.ilike(f"%{query}%"),
                    Case.court.ilike(f"%{query}%"),
                )
            )
            .all()
        )

    @staticmethod
    def update(db: Session, case: Case, data: dict):
        for key, value in data.items():
            setattr(case, key, value)
        db.commit()
        db.refresh(case)
        return case

    @staticmethod
    def delete(db: Session, case: Case):
        db.delete(case)
        db.commit()

    @staticmethod
    def get_by_status(db: Session, status: str):
        return (
            db.query(Case).filter(Case.status == status).order_by(Case.id.desc()).all()
        )

    @staticmethod
    def get_statistics(db: Session):
        total = db.query(Case).count()

        draft = db.query(Case).filter(Case.status == "Draft").count()

        open_cases = db.query(Case).filter(Case.status == "Open").count()

        closed = db.query(Case).filter(Case.status == "Closed").count()

        return {
            "total": total,
            "draft": draft,
            "open": open_cases,
            "closed": closed,
        }
