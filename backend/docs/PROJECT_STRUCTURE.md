# Project Structure

This project is a FastAPI backend with SQLAlchemy models and Alembic migrations. Keep feature code organized by responsibility so the app stays easy to grow.

## Folder Map

```text
OneLedger/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app creation and controller registration
│   │   ├── controllers/         # HTTP endpoints grouped by feature
│   │   ├── core/                # Shared infrastructure: settings, database setup
│   │   ├── dependencies/        # Reusable FastAPI dependencies
│   │   ├── dtos/                # Request and response DTO classes
│   │   ├── middlewares/         # App-wide request/response middleware
│   │   ├── models/              # SQLAlchemy database models
│   │   ├── services/            # Business logic used by controllers
│   │   └── utils/               # Small reusable helper functions
│   ├── alembic/
│   │   ├── env.py               # Alembic migration environment
│   │   └── versions/            # Database migration files
│   ├── docs/
│   │   └── PROJECT_STRUCTURE.md # This guide
│   ├── .env.example             # Example backend environment variables
│   ├── alembic.ini              # Alembic configuration
│   └── README.md                # Backend overview and quick start
├── frontend/
│   └── README.md                # UI app placeholder
├── .gitignore
└── README.md                    # Workspace overview
```

## Request Flow

```text
Client request
  -> app/main.py
  -> app/controllers/<feature>_controller.py
  -> app/dtos/request/<feature>_request.py
  -> app/services/<feature>_service.py
  -> app/models/<feature>.py
  -> database
  -> app/dtos/response/<feature>_response.py
  -> app/dtos/response/response_envelope.py
```

The controller should handle HTTP concerns. Request DTOs describe incoming payloads. Services handle business rules. Models describe database tables. Response DTOs describe outgoing payloads. Every successful response should use the shared response envelope.

## What Goes Where

`app/main.py`
: Create the FastAPI app and include controller routers. Keep this file small.

`app/core/`
: Put app-wide infrastructure here. Examples: settings, database engine/session setup, security configuration.

`app/dependencies/`
: Put reusable FastAPI dependencies here. Examples: current user, database session wrapper, permission checks.

`app/controllers/`
: Put API endpoints here. Controllers should validate inputs, call services, and return response envelopes.

`app/dtos/request/`
: Put request DTOs here. These classes describe incoming API payloads, such as `CreateBusinessRequest`.

`app/dtos/response/`
: Put response DTOs and shared response wrappers here. Use `ResponseEnvelope[T]` for consistent API responses.

`app/models/`
: Put SQLAlchemy models here. One file per domain area is a good default, such as `business.py`, `invoice.py`, or `customer.py`.

`app/services/`
: Put application logic here. Services are where you create records, run calculations, coordinate multiple models, or apply business rules.

`app/utils/`
: Put small stateless helpers here only when they are genuinely shared.

`alembic/versions/`
: Put database migrations here. Do not edit old migrations after they have been applied to shared environments unless you know every database can be reset.

## Adding A New Feature

For a new feature named `invoice`, use this shape:

```text
app/models/invoice.py
app/dtos/request/invoice_request.py
app/dtos/response/invoice_response.py
app/services/invoice_service.py
app/controllers/invoice_controller.py
```

Then:

1. Define the database table in `app/models/invoice.py`.
2. Define request DTOs in `app/dtos/request/invoice_request.py`.
3. Define response DTOs in `app/dtos/response/invoice_response.py`.
4. Put create/read/update/delete logic in `app/services/invoice_service.py`.
5. Expose API endpoints in `app/controllers/invoice_controller.py`.
6. Return all successful responses as `ResponseEnvelope[InvoiceResponse]` or `ResponseEnvelope[List[InvoiceResponse]]`.
7. Import and include the controller router in `app/main.py`.
8. Import the model in `alembic/env.py` so migrations can detect it.
9. Generate and review an Alembic migration.

## Response Envelope

All successful controller responses should use this shape:

```json
{
  "status_code": 200,
  "message": "Operation completed successfully",
  "result": {}
}
```

For list endpoints, `result` should be an array:

```json
{
  "status_code": 200,
  "message": "Records fetched successfully",
  "result": []
}
```

Errors are handled centrally and use the same envelope shape:

```json
{
  "status_code": 404,
  "message": "Business not found",
  "result": null
}
```

Use `ResponseEnvelope[T]` and `build_response(...)` from `app/dtos/response/response_envelope.py` so the result type and response shape stay clear across the project. Register shared exception handlers in `app/core/exception_handlers.py` instead of adding repeated try/except blocks to every controller.

Unexpected server errors are caught by `app/middlewares/error_handler_middleware.py`.

## Current API Surface

`POST /api/businesses/`
: Creates a business using the required business DTO.

`GET /api/businesses/`
: Returns businesses from the database.

`GET /api/businesses/{business_id}`
: Returns one business from the database.

## Current Data Model

`Business`
: Stores basic business profile information: name, business type, GST number, phone, email, and address.

## Cleanup Notes

- `venv/` and `__pycache__/` are generated files and should not be committed.
- The repo currently has two business migrations. The first is empty, and the second creates the `businesses` table. This is okay for local development, but future migrations should have clear names and only one purpose each.
- Keep `.env` private. Use `.env.example` to document required environment variables.
