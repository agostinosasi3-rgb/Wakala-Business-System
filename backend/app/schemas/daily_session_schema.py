from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ProviderFloatInput(BaseModel):
    provider_id: int
    opening_float: float

class SessionStartCreate(BaseModel):
    opening_cash: float
    provider_floats: List[ProviderFloatInput]

class ProviderFloatClosing(BaseModel):
    provider_id: int
    closing_float: float

class SessionCloseInput(BaseModel):
    closing_cash: float
    provider_floats: List[ProviderFloatClosing]

class DailySessionResponse(BaseModel):
    id: int
    date: datetime
    opening_cash: float
    closing_cash: Optional[float] = None
    status: str
    total_variance: Optional[float] = 0.0

    class Config:
        from_attributes = True