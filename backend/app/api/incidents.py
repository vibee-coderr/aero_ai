from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db 
from app.models.incident import Incident
from datetime import datetime

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)

@router.get("/")
def get_incidents(
    db: Session = Depends(get_db)
):
    return db.query(Incident).all()
@router.patch("/{incident_id}/resolve")
def resolve_incident(
    incident_id: int,
    db: Session = Depends(get_db)
):

    incident = db.query(Incident).filter(
        Incident.id == incident_id
    ).first()

    incident.status = "RESOLVED"
    incident.resolved_at = datetime.utcnow()

    db.commit()

    return {
        "message": "Incident Resolved"
    }