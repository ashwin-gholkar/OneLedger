# Getting Started

Use this file when setting up or working on the OneLedger project.

## Project Layout

```text
OneLedger/
├── backend/     # FastAPI backend
├── frontend/    # React UI
└── README.md
```

## Backend Setup

Run backend commands from the `backend/` folder.

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Update `.env` with your local database URL.

```bash
alembic upgrade head
uvicorn app.main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

API docs will be available at:

```text
http://127.0.0.1:8000/docs
```

## Frontend Setup

The UI will be React. Use Vite for the React app.

If the `frontend/` folder is still empty except for its README, create the React app with:

```bash
cd frontend
npm create vite@latest . -- --template react
npm install
npm run dev
```

Frontend will usually run at:

```text
http://127.0.0.1:5173
```

For later work, start the existing React app with:

```bash
cd frontend
npm install
npm run dev
```

## Daily Development Commands

Start backend:

```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload
```

Start frontend:

```bash
cd frontend
npm run dev
```

Run database migrations:

```bash
cd backend
source .venv/bin/activate
alembic upgrade head
```

Create a new migration after model changes:

```bash
cd backend
source .venv/bin/activate
alembic revision --autogenerate -m "describe change"
alembic upgrade head
```

## API Response Shape

Successful API responses should use the shared response envelope:

```json
{
  "status_code": 200,
  "message": "Operation completed successfully",
  "result": {}
}
```

List responses should use:

```json
{
  "status_code": 200,
  "message": "Records fetched successfully",
  "result": []
}
```

Error responses should use the same shape:

```json
{
  "status_code": 404,
  "message": "Business not found",
  "result": null
}
```
