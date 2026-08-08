from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.transaction import Transaction, TransactionType
from app.models.daily_sesssion import DailySession
from app.models.tarrif import Tariff
from app.models.user import User
from app.schemas.transaction_schema import TransactionCreate

class TransactionService:
    def __init__(self, db: Session):
        self.db = db

    def _calculate_commission(self, provider_id: int, amount: float) -> float:
        tariff = self.db.query(Tariff).filter(
            Tariff.provider_id == provider_id,
            Tariff.min_amount <= amount,
            Tariff.max_amount >= amount
        ).first()
        return float(tariff.agent_commission) if tariff else 0.0

    def create_transaction(self, user: User, data: TransactionCreate) -> Transaction:
        session = self.db.query(DailySession).filter(
            DailySession.user_id == user.id,
            DailySession.status == "OPEN"
        ).first()

        if not session:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Huwezi kurekodi muamala bila kufungua session ya siku kwanza."
            )

        commission = self._calculate_commission(data.provider_id, data.amount)

        new_transaction = Transaction(
            session_id=session.id,
            user_id=user.id,
            provider_id=data.provider_id,
            transaction_type=data.transaction_type,
            amount=data.amount,
            estimated_commission=commission,
            reference_number=data.reference_number
        )

        self.db.add(new_transaction)
        self.db.commit()
        self.db.refresh(new_transaction)
        return new_transaction