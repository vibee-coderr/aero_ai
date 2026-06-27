from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.telemetry import TelemetryEvent
from app.schemas.telemetry import TelemetryCreate

router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry"]
)

@router.post("/")
def create_event(
    event: TelemetryCreate,
    db: Session = Depends(get_db)
):

    telemetry = TelemetryEvent(
        service_name=event.service_name,
        event_type=event.event_type,
        severity=event.severity,
        description=event.description
    )

    db.add(telemetry)

    db.commit()

    db.refresh(telemetry)

    return {
        "message": "Telemetry Event Stored",
        "event_id": telemetry.id
    }
@router.get("/")
def get_events(
    db: Session = Depends(get_db)
):

    events = db.query(
        TelemetryEvent
    ).all()

    return events