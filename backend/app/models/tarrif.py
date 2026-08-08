from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Tariff(Base):
    __tablename__ = "tariffs"

    id = Column(Integer, primary_key=True, index=True)
    provider_id = Column(Integer, ForeignKey("providers.id"), nullable=False)
    min_amount = Column(Numeric(12, 2), nullable=False)
    max_amount = Column(Numeric(12, 2), nullable=False)
    agent_commission = Column(Numeric(12, 2), nullable=False)

    provider = relationship("Provider", back_populates="tariffs")