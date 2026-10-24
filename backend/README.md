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


## Configuration

Connectly reads application settings from environment variables
using the `CONNECTLY_` prefix.

Copy the example configuration for local development:

    cp .env.example .env

Available settings:

| Variable | Default | Purpose |
|---|---|---|
| CONNECTLY_APP_NAME | Connectly API | Application name |
| CONNECTLY_APP_DESCRIPTION | Backend API for the Connectly video calling application. | API description |
| CONNECTLY_APP_VERSION | 0.1.0 | API version |
| CONNECTLY_DEBUG | false | Enable debug mode |

The `.env` file is for local configuration only and must not
be committed. `.env.example` documents the available settings.


## Health checks

| Endpoint | Purpose | Expected response |
|---|---|---|
| `GET /health/live` | Checks whether the application is responding | `{"status": "alive"}` |
| `GET /health/ready` | Checks whether the application is ready to accept requests | `{"status": "ready"}` |

Currently, the application has no external dependencies required for
readiness. The readiness check can be extended when we introduce
dependencies such as a database.

## Running tests

Install development dependencies:

    pip install -r requirements-dev.txt

Run the test suite:

    python -m pytest -v