from fastapi import FastAPI
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.app_version,
    debug=settings.debug
)


@app.get("/")
async def root():
    return {
        "name": settings.app_name,
        "description": settings.app_description,
        "version": settings.app_version,
        "debug": settings.debug,
        "status": "running",
    }


@app.get("/health/live", tags=["health"])
async def liveness():
    return {"status": "alive"}


@app.get("/health/ready", tags=["health"])
async def readiness():
    return {"status": "ready"}