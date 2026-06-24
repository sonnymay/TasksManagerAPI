# Changelog

All notable changes to TasksManagerAPI are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [Unreleased]

### Planned
- JWT bearer token authentication (register + login endpoints)
- Pagination and filtering on `GET /tasks/` (`?skip`, `?limit`, `?status`, `?q`)
- Due date and priority fields on the Task model
- Alembic migration workflow for schema evolution

---

## [1.0.0] — Initial release

### Added
- `GET /tasks/` — list all tasks
- `POST /tasks/` — create a task (title required; description optional)
- `GET /tasks/{task_id}` — get a single task by ID
- `PUT /tasks/{task_id}` — update title, description, or completion status
- `PATCH /tasks/{task_id}/complete` — mark a task as completed
- `DELETE /tasks/{task_id}` — delete a task
- Pydantic request and response schemas with automatic validation
- SQLAlchemy ORM model backed by SQLite (local) or PostgreSQL (production via `DATABASE_URL`)
- Auto-generated Swagger UI at `/docs` and ReDoc at `/redoc`
- GitHub Actions CI running `pytest` and Python compile checks on every push
- Docker support via `Dockerfile` and `docker-compose.yml`
- Render deployment config via `render.yaml`
