from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.core.database import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    severity = Column(String)

    status = Column(String, default="OPEN")

    created_at = Column(DateTime, default=datetime.utcnow)

    resolved_at = Column(DateTime, nullable=True)