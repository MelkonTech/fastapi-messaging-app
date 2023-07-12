from app.configs.database import Base
from sqlalchemy import TIMESTAMP, Column, String, Integer
from sqlalchemy.sql import func


class StatsMessage(Base):
    __tablename__ = "statsmessage"
    uuid = Column(String, nullable=False, primary_key=True)
    customerId = Column(Integer, nullable=False)
    message_type = Column(String, nullable=False)
    amount = Column(String, nullable=False)
    createdAt = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    updatedAt = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())
