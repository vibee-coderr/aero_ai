from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.core.config import settings
from app.api.telemetry import router as telemetry_router
from app.api.incidents import router as incident_router
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)
app.include_router(auth_router)
app.include_router(
    telemetry_router
)
app.include_router(incident_router)

@app.get("/")
def root():
    return {
        "message": "Aero.ai Backend Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }