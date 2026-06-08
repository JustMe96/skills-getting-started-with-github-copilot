# Backend Documentation

## Overview

This repository contains a small FastAPI backend for the Mergington High School
activities API. The FastAPI application lives in `src/app.py` and exposes a few
simple endpoints to list activities and manage signups.

## Requirements

- Python 3.9+ (recommended)
- See `requirements.txt` for runtime and test dependencies. `pytest` is used
  for the test suite.

## Running the app (development)

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the app with uvicorn:

```bash
uvicorn src.app:app --reload
```

The static UI is mounted at `/static` and the root redirects to
`/static/index.html`.

## Available endpoints (brief)

- `GET /` — Redirects to `/static/index.html`.
- `GET /activities` — Returns the activities dictionary (JSON).
- `POST /activities/{activity_name}/signup` — Sign up a student. Query
  parameter: `email` (string).
- `DELETE /activities/{activity_name}/participants` — Remove a participant by
  `email` (query parameter).

Example: sign up a student

```bash
curl -X POST "http://localhost:8000/activities/Chess%20Club/signup?email=me@example.com"
```

## Testing

- Tests live under the `tests/` directory. We use `pytest` and a
  `TestClient` fixture in `tests/conftest.py`.
- Run the test suite:

```bash
pytest -q
```

Notes:
- Import the FastAPI `app` for tests as `from src.app import app` (the project
  root is on `PYTHONPATH` via `pytest.ini`).
