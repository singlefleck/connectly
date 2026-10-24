from fastapi import FastAPI

app = FastAPI(
    title="Connectly API",
    description="Backend API for the Connectly video calling application.",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "name": "Connectly API",
        "status": "running",
    }