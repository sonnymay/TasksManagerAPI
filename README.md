# 🗂️ Task Manager API

A simple and clean RESTful API for managing tasks, built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL (or SQLite)**.  
It supports full CRUD operations — create, read, update, complete, and delete tasks.

---

## 🚀 Features
- 🧱 RESTful API with FastAPI
- 💾 Database integration using SQLAlchemy ORM
- ⚙️ Environment-based configuration for SQLite or PostgreSQL
- 🌐 CORS enabled for frontend integration
- 📜 Auto-generated API docs via Swagger (`/docs`)

---

## 📂 Tech Stack
- **Backend:** FastAPI
- **Database:** SQLite (local) / PostgreSQL (production)
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Server:** Uvicorn

---

## 🧩 Endpoints Overview
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/tasks/` | Fetch all tasks |
| POST | `/tasks/` | Create a new task |
| GET | `/tasks/{id}` | Retrieve a task by ID |
| PUT | `/tasks/{id}` | Update a task |
| PATCH | `/tasks/{id}/complete` | Mark a task as complete |
| DELETE | `/tasks/{id}` | Delete a task |

---

## ⚙️ Installation

```bash
git clone https://github.com/sonnymay/TasksManagerAPI.git
cd TasksManagerAPI
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
