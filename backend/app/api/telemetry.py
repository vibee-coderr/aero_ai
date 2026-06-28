from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.telemetry import TelemetryEvent
from app.schemas.telemetry import TelemetryCreate
from app.models.incident import Incident

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
    if event.severity.upper() == "HIGH":

        incident = Incident(
        title=f"{event.service_name} Failure",
        severity=event.severity,
        status="OPEN"
    )

        db.add(incident)
        db.commit()
    

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