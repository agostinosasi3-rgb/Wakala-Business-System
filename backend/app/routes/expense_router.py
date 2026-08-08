from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.models.daily_sesssion import DailySession
from app.models.expense import Expense
from app.schemas.expenses_schema import ExpenseCreate, ExpenseResponse

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/", response_model=ExpenseResponse)
def add_expense(
    data: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    session = db.query(DailySession).filter(
        DailySession.user_id == current_user.id,
        DailySession.status == "OPEN"
    ).first()

    if not session:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Fungua session kwanza kabla ya kurekodi matumizi."
        )

    new_expense = Expense(
        session_id=session.id,
        user_id=current_user.id,
        title=data.title,
        amount=data.amount,
        description=data.description
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense