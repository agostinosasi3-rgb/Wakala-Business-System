from pydantic import BaseModel
from typing import Dict

class WeeklyReportResponse(BaseModel):
    start_date: str
    end_date: str
    total_cash_in_volume: float
    total_cash_out_volume: float
    total_commission_earned: float
    total_expenses: float
    total_shortages: float
    net_profit_loss: float
    provider_breakdown: Dict[str, float]