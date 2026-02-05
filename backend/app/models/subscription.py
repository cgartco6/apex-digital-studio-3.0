from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database.base import Base

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    plan = Column(String)
    provider = Column(String)
    status = Column(String)
    started_at = Column(DateTime, default=datetime.utcnow)
