from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    description: Optional[str] = None

class ExpenseResponse(BaseModel):
    id: int
    session_id: int
    title: str
    amount: float
    description: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True