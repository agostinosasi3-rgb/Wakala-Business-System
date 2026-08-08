from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.schemas.report_schema import WeeklyReportResponse
from app.services.report_service import ReportService

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/weekly", response_model=WeeklyReportResponse)
def get_weekly_report(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = ReportService(db)
    return service.generate_weekly_report(current_user.id)