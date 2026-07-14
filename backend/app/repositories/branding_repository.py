from sqlalchemy.orm import Session

from app.models.branding import Branding


class BrandingRepository:

    @staticmethod
    def get(db: Session):
        return db.query(Branding).first()

    @staticmethod
    def create(db: Session, data: dict):
        branding = Branding(**data)
        db.add(branding)
        db.commit()
        db.refresh(branding)
        return branding

    @staticmethod
    def update(db: Session, branding: Branding, data: dict):
        for key, value in data.items():
            if value is not None:
                setattr(branding, key, value)

        db.add(branding)
        db.commit()
        db.refresh(branding)
        return branding

    @staticmethod
    def save(db: Session, data: dict):
        branding = BrandingRepository.get(db)

        if branding is None:
            return BrandingRepository.create(db, data)

        return BrandingRepository.update(db, branding, data)

    @staticmethod
    def delete(db: Session):
        branding = BrandingRepository.get(db)

        if branding:
            db.delete(branding)
            db.commit()
