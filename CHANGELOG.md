# Changelog

All notable changes to TasksManagerAPI are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### Planned
- JWT authentication middleware
- Rate limiting per API key
- OpenAPI documentation improvements
- Task tagging and label-based filtering

---

## [1.1.0] – 2026-06-24

### Added
- `priority` field on Task model (`low` | `medium` | `high`)
- `due_date` field on Task model (ISO 8601 date)
- `completed`, `priority`, `due_before` query filters on `GET /tasks/`
- Default `limit` reduced from 100 to 20; max capped at 200
- `TaskCreate` schema updated to accept priority and due_date

---

## [1.0.0] – 2026-06-01

### Added
- FastAPI project scaffold with SQLAlchemy + SQLite
- `Task` model: id, title, description, completed
- CRUD endpoints: `POST /tasks/`, `GET /tasks/`, `GET /tasks/{id}`
- `PUT /tasks/{id}` – full update
- `PATCH /tasks/{id}/complete` – mark completed
- `DELETE /tasks/{id}`
- Pagination via `skip` / `limit` query params on `GET /tasks/`
- Pydantic v2 schemas with `from_attributes=True`
