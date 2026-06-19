# OneLedger

OneLedger is organized as a full-stack workspace with separate backend and frontend folders.

## Folder Layout

```text
OneLedger/
├── backend/     # FastAPI API, database models, Alembic migrations
├── frontend/    # UI application lives here
├── GETTING_STARTED.md
├── .gitignore
└── README.md
```

## Getting Started

Use [GETTING_STARTED.md](GETTING_STARTED.md) for backend and React frontend setup commands.

## Backend

The backend is in `backend/`.

```bash
cd backend
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

See `backend/docs/PROJECT_STRUCTURE.md` for the backend architecture.

## Frontend

The frontend is in `frontend/`. It is intended to be a React app.
