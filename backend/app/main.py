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