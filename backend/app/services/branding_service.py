from sqlalchemy.orm import Session

from app.repositories.branding_repository import BrandingRepository


class BrandingService:

    @staticmethod
    def get(db: Session):
        return BrandingRepository.get(db)

    @staticmethod
    def save(db: Session, data: dict):
        return BrandingRepository.save(db, data)

    @staticmethod
    def update(db: Session, data: dict):
        branding = BrandingRepository.get(db)

        if branding is None:
            return BrandingRepository.create(db, data)

        return BrandingRepository.update(db, branding, data)

    @staticmethod
    def delete(db: Session):
        BrandingRepository.delete(db)

    @staticmethod
    def get_invoice_template(db: Session) -> str:
        branding = BrandingRepository.get(db)

        if branding is None:
            return "classic"

        return branding.default_invoice_template

    @staticmethod
    def get_primary_color(db: Session) -> str:
        branding = BrandingRepository.get(db)

        if branding is None:
            return "#1F4E79"

        return branding.primary_color

    @staticmethod
    def get_secondary_color(db: Session) -> str:
        branding = BrandingRepository.get(db)

        if branding is None:
            return "#404040"

        return branding.secondary_color

    @staticmethod
    def get_logo(db: Session):
        branding = BrandingRepository.get(db)

        if branding is None:
            return None

        return branding.logo_path

    @staticmethod
    def get_signature(db: Session):
        branding = BrandingRepository.get(db)

        if branding is None:
            return None

        return branding.signature_path
