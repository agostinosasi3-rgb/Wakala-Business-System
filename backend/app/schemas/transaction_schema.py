from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.transaction import TransactionType

class TransactionCreate(BaseModel):
    provider_id: int
    transaction_type: TransactionType
    amount: float
    reference_number: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    session_id: int
    provider_id: int
    transaction_type: TransactionType
    amount: float
    estimated_commission: float
    reference_number: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True