import os

os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import database, models
from app.main import app


@pytest.fixture()
def client(tmp_path):
    engine = create_engine(
        f"sqlite:///{tmp_path / 'tasks-test.db'}",
        connect_args={"check_same_thread": False},
    )
    testing_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    models.Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = testing_session()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[database.get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()


def test_task_crud_flow(client):
    create_response = client.post(
        "/tasks/",
        json={"title": "Ship portfolio polish", "description": "Make GitHub recruiter-ready"},
    )
    assert create_response.status_code == 200
    task = create_response.json()
    assert task["title"] == "Ship portfolio polish"
    assert task["completed"] is False

    list_response = client.get("/tasks/")
    assert list_response.status_code == 200
    assert list_response.json() == [task]

    update_response = client.put(
        f"/tasks/{task['id']}",
        json={"title": "Ship tests", "description": "Cover the API flow"},
    )
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Ship tests"

    complete_response = client.patch(f"/tasks/{task['id']}/complete")
    assert complete_response.status_code == 200
    assert complete_response.json()["completed"] is True

    delete_response = client.delete(f"/tasks/{task['id']}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Task deleted successfully"}

    assert client.get(f"/tasks/{task['id']}").status_code == 404


def test_missing_task_returns_404(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}
