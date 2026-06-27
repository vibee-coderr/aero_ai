from pydantic import BaseModel

class IncidentResponse(BaseModel):
    id: int
    title: str
    severity: str
    status: str

    class Config:
        from_attributes = True