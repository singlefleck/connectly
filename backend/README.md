# Connectly Backend

Python backend for the Connectly video calling application.

## Requirements

- Python 3.12+
- pip

## Setup

From the backend directory:

    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

## Run locally

    uvicorn app.main:app --reload

## API documentation

- Interactive docs: http://127.0.0.1:8000/docs
- OpenAPI schema: http://127.0.0.1:8000/openapi.json
- Root endpoint: http://127.0.0.1:8000/