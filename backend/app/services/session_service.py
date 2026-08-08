from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.daily_sesssion import DailySession, DailySessionFloat
from app.models.user import User
from app.schemas.daily_session_schema import SessionStartCreate, SessionCloseInput

class SessionService:
    def __init__(self, db: Session):
        self.db = db

    def start_session(self, user: User, session_input: SessionStartCreate) -> DailySession:
        active_session = self.db.query(DailySession).filter(
            DailySession.user_id == user.id,
            DailySession.status == "OPEN"
        ).first()
        
        if active_session:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Una session iliyofunguliwa tayari. Funga kwanza ndipo uanzishe mpya."
            )

        new_session = DailySession(
            user_id=user.id,
            opening_cash=session_input.opening_cash,
            status="OPEN"
        )
        self.db.add(new_session)
        self.db.flush()

        for p_float in session_input.provider_floats:
            session_float = DailySessionFloat(
                session_id=new_session.id,
                provider_id=p_float.provider_id,
                opening_float=p_float.opening_float
            )
            self.db.add(session_float)

        self.db.commit()
        self.db.refresh(new_session)
        return new_session