# OneLedger

This folder contains the OneLedger FastAPI backend for business/accounting workflows. The root project also has a separate `frontend/` folder for UI code.

## Current Scope

- FastAPI application setup in `app/main.py`
- SQLAlchemy database setup in `app/core/database.py`
- Environment-based settings in `app/core/config.py`
- Business database model in `app/models/business.py`
- Business API controller in `app/controllers/business_controller.py`
- Request DTOs in `app/dtos/request`
- Response DTOs in `app/dtos/response`
- Shared response envelope in `app/dtos/response/response_envelope.py`
- Database migrations in `alembic/versions`

## Suggested Local Setup

Run backend commands from this `backend/` folder.

1. Create and activate a virtual environment.
2. Install the project dependencies.
3. Create `.env` from `.env.example`.
4. Run database migrations.
5. Start the FastAPI app.

```bash
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

## Project Guide

Read [docs/PROJECT_STRUCTURE.md](docs/PROJECT_STRUCTURE.md) before adding new features. It explains the folder responsibilities, request flow, and the recommended pattern for adding modules.
