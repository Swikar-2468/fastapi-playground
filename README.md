# FastAPI Playground

A hands-on learning project for exploring FastAPI with a structured application layout, database integration via SQLAlchemy, and schema migrations managed by Alembic.

## Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** — Modern, high-performance Python web framework
- **SQLAlchemy** — ORM for database interaction
- **Alembic** — Database schema migration tool
- **Uvicorn** — ASGI server for running the app
- **Pydantic** — Data validation and settings management

## Project Structure

```
fastapi-playground/
├── app/                  # Core application code
│   ├── main.py           # FastAPI app entry point
│   ├── models.py         # SQLAlchemy ORM models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # Database CRUD operations
│   ├── database.py       # DB connection & session setup
│   └── routers/          # API route handlers
├── alembic/              # Database migration files
│   └── versions/         # Migration scripts
├── alembic.ini           # Alembic configuration
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.10+
- A running database (PostgreSQL recommended)

### Installation

```bash
# Clone the repo
git clone https://github.com/Swikar-2468/fastapi-playground.git
cd fastapi-playground

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn sqlalchemy alembic psycopg2-binary
```

### Database Setup

Update the `DATABASE_URL` in your environment or `database.py` to point to your database, then apply migrations:

```bash
alembic upgrade head
```

### Running the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Interactive Docs

FastAPI generates interactive documentation automatically:

| UI | URL |
|---|---|
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |

## Database Migrations

```bash
# Create a new migration after changing models
alembic revision --autogenerate -m "describe your change"

# Apply all pending migrations
alembic upgrade head

# Roll back the last migration
alembic downgrade -1
```

## License

This project is for learning purposes. Feel free to explore and experiment.