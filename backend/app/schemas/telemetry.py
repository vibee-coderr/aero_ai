from pydantic import BaseModel


class TelemetryCreate(BaseModel):

    service_name: str
    event_type: str
    severity: str
    description: str