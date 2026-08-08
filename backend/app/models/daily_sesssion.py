from sqlalchemy import Column, Integer, Numeric, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class DailySession(Base):
    __tablename__ = "daily_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    
    opening_cash = Column(Numeric(12, 2), nullable=False)
    midday_cash = Column(Numeric(12, 2), nullable=True)
    closing_cash = Column(Numeric(12, 2), nullable=True)
    
    status = Column(String(20), default="OPEN") # OPEN, CLOSED
    total_variance = Column(Numeric(12, 2), default=0.0)

    user = relationship("User", back_populates="sessions")
    provider_floats = relationship("DailySessionFloat", back_populates="session", cascade="all, delete-orphan")
    transactions = relationship("Transaction", back_populates="session")
    expenses = relationship("Expense", back_populates="session")

class DailySessionFloat(Base):
    __tablename__ = "daily_session_floats"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("daily_sessions.id"), nullable=False)
    provider_id = Column(Integer, ForeignKey("providers.id"), nullable=False)
    
    opening_float = Column(Numeric(12, 2), nullable=False)
    midday_float = Column(Numeric(12, 2), nullable=True)
    closing_float = Column(Numeric(12, 2), nullable=True)

    session = relationship("DailySession", back_populates="provider_floats")
    provider = relationship("Provider", back_populates="session_floats")