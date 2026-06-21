# Task Manager API

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=flat-square&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-compatible-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![CI](https://github.com/sonnymay/TasksManagerAPI/actions/workflows/ci.yml/badge.svg)

A small RESTful task-management API built with FastAPI, SQLAlchemy, and Pydantic. It supports task CRUD, completion updates, automatic Swagger docs, and local SQLite development with a `DATABASE_URL` path for production databases.

## Live Swagger Demo

Deploy to Render/Railway to generate a live Swagger URL.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

After deployment, open `/docs` on the deployed service URL for Swagger UI.

## Features

- Create, list, read, update, complete, and delete tasks
- Pydantic request and response schemas
- SQLAlchemy model and session management
- SQLite by default, with PostgreSQL-compatible `DATABASE_URL` configuration
- Swagger UI at `/docs` and ReDoc at `/redoc`
- GitHub Actions CI running pytest and Python compile checks

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Database | SQLite locally, PostgreSQL-compatible via `DATABASE_URL` |
| Server | Uvicorn |
| Testing | pytest + httpx |
| CI | GitHub Actions |

## Quickstart

```bash
git clone https://github.com/sonnymay/TasksManagerAPI.git
cd TasksManagerAPI
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Open `http://localhost:8000/docs` for the interactive Swagger UI.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health-style welcome message |
| `GET` | `/tasks/` | List all tasks |
| `POST` | `/tasks/` | Create a task |
| `GET` | `/tasks/{task_id}` | Get one task |
| `PUT` | `/tasks/{task_id}` | Update a task |
| `PATCH` | `/tasks/{task_id}/complete` | Mark a task completed |
| `DELETE` | `/tasks/{task_id}` | Delete a task |

## Running Tests

```bash
pytest
```

## Project Structure

```text
app/
  main.py          # FastAPI app, CORS, router wiring
  database.py      # SQLAlchemy engine/session setup
  models.py        # SQLAlchemy Task model
  schemas.py       # Pydantic request/response schemas
  routes/tasks.py  # Task CRUD routes
tests/
  test_tasks.py    # API tests
```

## What This Code Shows

- FastAPI routing with dependency-injected database sessions
- Clear separation between SQLAlchemy models and Pydantic schemas
- Environment-based database configuration
- Small, readable API surface with automated OpenAPI docs
- CI-backed backend project hygiene

