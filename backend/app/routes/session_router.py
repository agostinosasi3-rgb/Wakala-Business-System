from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.schemas.daily_session_schema import SessionStartCreate, DailySessionResponse
from app.services.session_service import SessionService

router = APIRouter(prefix="/sessions", tags=["Daily Sessions"])

@router.post("/start", response_model=DailySessionResponse)
def start_session(
    session_input: SessionStartCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    session_service = SessionService(db)
    return session_service.start_session(current_user, session_input)