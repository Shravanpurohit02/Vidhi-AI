from sqlalchemy.orm import Session

from app.repositories.report_repository import ReportRepository


class ReportService:

    @staticmethod
    def outstanding_invoices(db: Session):
        return ReportRepository.outstanding_invoices(db)

    @staticmethod
    def paid_invoices(db: Session):
        return ReportRepository.paid_invoices(db)

    @staticmethod
    def overdue_invoices(db: Session):
        return ReportRepository.overdue_invoices(db)
