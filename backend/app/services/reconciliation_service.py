from sqlalchemy.orm import Session
from app.models.daily_sesssion import DailySession
from app.models.transaction import Transaction, TransactionType
from app.models.expense import Expense

class ReconciliationService:
    def __init__(self, db: Session):
        self.db = db

    def calculate_daily_reconciliation(self, session_id: int, closing_cash: float) -> float:
        session = self.db.query(DailySession).filter(DailySession.id == session_id).first()
        if not session:
            return 0.0

        transactions = self.db.query(Transaction).filter(Transaction.session_id == session_id).all()
        expenses = self.db.query(Expense).filter(Expense.session_id == session_id).all()

        total_cash_in = sum(t.amount for t in transactions if t.transaction_type == TransactionType.CASH_OUT) # Cash Out Inaleta Cash
        total_cash_out = sum(t.amount for t in transactions if t.transaction_type == TransactionType.CASH_IN) # Cash In Inapunguza Cash
        total_expenses = sum(e.amount for e in expenses)

        expected_cash = float(session.opening_cash) + float(total_cash_in) - float(total_cash_out) - float(total_expenses)
        variance = float(closing_cash) - expected_cash
        return variance