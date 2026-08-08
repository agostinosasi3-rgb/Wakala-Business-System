from sqlalchemy import Column, Integer, Numeric, DateTime, ForeignKey, String, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.core.database import Base

class TransactionType(str, enum.Enum):
    CASH_IN = "CASH_IN"     # Kuweka Pesa (Float In, Cash Out)
    CASH_OUT = "CASH_OUT"   # Kutoa Pesa (Float Out, Cash In)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("daily_sessions.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    provider_id = Column(Integer, ForeignKey("providers.id"), nullable=False)
    
    transaction_type = Column(Enum(TransactionType), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    estimated_commission = Column(Numeric(12, 2), default=0.0)
    reference_number = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    session = relationship("DailySession", back_populates="transactions")
    user = relationship("User", back_populates="transactions")
    provider = relationship("Provider", back_populates="transactions")