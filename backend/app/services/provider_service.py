from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List
from app.models.provider import Provider
from app.schemas.provider_schema import ProviderCreate

class ProviderService:
    def __init__(self, db: Session):
        self.db = db

    def get_all_providers(self) -> List[Provider]:
        return self.db.query(Provider).filter(Provider.is_active == True).all()

    def create_provider(self, provider_data: ProviderCreate) -> Provider:
        existing = self.db.query(Provider).filter(Provider.code == provider_data.code).first()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Provider huyu yupo tayari."
            )
        new_provider = Provider(name=provider_data.name, code=provider_data.code)
        self.db.add(new_provider)
        self.db.commit()
        self.db.refresh(new_provider)
        return new_provider