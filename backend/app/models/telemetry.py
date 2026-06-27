from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.core.database import Base


class TelemetryEvent(Base):

    __tablename__ = "telemetry_events"

    id = Column(Integer, primary_key=True)

    service_name = Column(String)

    event_type = Column(String)

    severity = Column(String)

    description = Column(String)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )