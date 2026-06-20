# Task Manager API

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=flat-square&logo=fastapi&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-compatible-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![tests](https://img.shields.io/badge/tests-passing-brightgreen?style=flat-square&logo=pytest&logoColor=white) ![CI](https://github.com/sonnymay/TasksManagerAPI/actions/workflows/ci.yml/badge.svg) ![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

A production-ready RESTful task management API with full CRUD, Pydantic validation, auto-generated Swagger docs, and an isolated pytest test suite. Runs on SQLite locally and PostgreSQL in production.

## Features

- **Full CRUD** - create, read, update, and delete tasks with title, description, priority, due date, and status
- - **Pydantic v2 validation** - strict request/response schemas with automatic error messages on bad input
  - - **Auto-generated docs** - Swagger UI at `/docs`, ReDoc at `/redoc` - zero manual spec writing
    - - **SQLAlchemy ORM** - clean model layer; swap SQLite for PostgreSQL with one env variable
      - - **CORS middleware** - ready for browser-based frontend integration
        - - **pytest test suite** - all CRUD endpoints covered against an isolated SQLite test database
          - - **GitHub Actions CI** - lint and tests run on every push to main
           
            - ## Tech Stack
           
            - | Layer | Technology |
            - |---|---|
            - | Framework | FastAPI 0.110+ |
            - | ORM | SQLAlchemy 2.0 |
            - | Validation | Pydantic v2 |
            - | Database | SQLite (dev) / PostgreSQL (prod) |
            - | Testing | pytest + httpx |
            - | CI | GitHub Actions |
           
            - ## Quickstart
           
            - ```bash
              git clone https://github.com/sonnymay/TasksManagerAPI.git
              cd TasksManagerAPI
              pip install -r requirements.txt
              uvicorn app.main:app --reload
              ```

              Then open **http://localhost:8000/docs** for the interactive Swagger UI.

              ## API Endpoints

              | Method | Endpoint | Description |
              |---|---|---|
              | `GET` | `/tasks` | List all tasks |
              | `POST` | `/tasks` | Create a task |
              | `GET` | `/tasks/{id}` | Get a task by ID |
              | `PUT` | `/tasks/{id}` | Update a task |
              | `DELETE` | `/tasks/{id}` | Delete a task |

              ## Running Tests

              ```bash
              pip install -r requirements-dev.txt
              pytest -v
              ```

              Tests use an isolated in-memory SQLite DB - no external dependencies required.

              ## Project Structure

              ```
              TasksManagerAPI/
              app/
                  main.py        - FastAPI app, CORS, router wiring
                  models.py      - SQLAlchemy ORM models
                  schemas.py     - Pydantic request/response schemas
                  routes/
                      tasks.py   - CRUD route handlers
              tests/
                  test_tasks.py  - pytest test suite
              requirements.txt
              requirements-dev.txt
              ```

              ## Design Patterns Demonstrated

              - **Dependency injection** for DB sessions via `Depends(get_db)`
              - - **Schema/model separation** - Pydantic schemas never bleed into SQLAlchemy models
                - - **Test isolation** - per-test DB state, no cross-test pollution
                  - - **CI gate** - tests must pass before merge
                   
                    - ## License
                   
                    - MIT
