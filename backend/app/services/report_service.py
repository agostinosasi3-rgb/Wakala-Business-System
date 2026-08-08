from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.models.transaction import Transaction, TransactionType
from app.models.expense import Expense
from app.models.daily_sesssion import DailySession

class ReportService:
    def __init__(self, db: Session):
        self.db = db

    def generate_weekly_report(self, user_id: int):
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=7)

        sessions = self.db.query(DailySession).filter(
            DailySession.user_id == user_id,
            DailySession.date >= start_date
        ).all()

        session_ids = [s.id for s in sessions]

        transactions = self.db.query(Transaction).filter(Transaction.session_id.in_(session_ids)).all() if session_ids else []
        expenses = self.db.query(Expense).filter(Expense.session_id.in_(session_ids)).all() if session_ids else []

        cash_in_volume = sum(t.amount for t in transactions if t.transaction_type == TransactionType.CASH_IN)
        cash_out_volume = sum(t.amount for t in transactions if t.transaction_type == TransactionType.CASH_OUT)
        total_commission = sum(t.estimated_commission for t in transactions)
        total_expenses = sum(e.amount for e in expenses)
        total_shortages = sum(abs(s.total_variance) for s in sessions if s.total_variance and s.total_variance < 0)

        net_profit = float(total_commission) - float(total_expenses) - float(total_shortages)

        return {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "total_cash_in_volume": float(cash_in_volume),
            "total_cash_out_volume": float(cash_out_volume),
            "total_commission_earned": float(total_commission),
            "total_expenses": float(total_expenses),
            "total_shortages": float(total_shortages),
            "net_profit_loss": float(net_profit),
            "provider_breakdown": {}
        }