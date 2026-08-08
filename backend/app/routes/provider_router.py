from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.provider_schema import ProviderCreate, ProviderResponse
from app.services.provider_service import ProviderService

router = APIRouter(prefix="/providers", tags=["Providers"])

@router.get("/", response_model=List[ProviderResponse])
def get_providers(db: Session = Depends(get_db)):
    service = ProviderService(db)
    return service.get_all_providers()

@router.post("/", response_model=ProviderResponse)
def create_provider(data: ProviderCreate, db: Session = Depends(get_db)):
    service = ProviderService(db)
    return service.create_provider(data)