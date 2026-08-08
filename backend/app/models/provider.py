from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False) # M-PESA, MIX_BY_YAS, AIRTEL_MONEY, TIGO_PESA
    code = Column(String(20), unique=True, nullable=False) # MPESA, MIX, AIRTEL, TIGO
    is_active = Column(Boolean, default=True)

    session_floats = relationship("DailySessionFloat", back_populates="provider")
    transactions = relationship("Transaction", back_populates="provider")
    tariffs = relationship("Tariff", back_populates="provider")