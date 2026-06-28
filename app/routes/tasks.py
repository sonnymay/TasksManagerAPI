import datetime
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from .. import models, schemas, database

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# --- Create Task ---
@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        due_date=task.due_date,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# --- Get All Tasks (with pagination + filtering) ---
@router.get("/", response_model=list[schemas.Task])
def get_tasks(
    skip: int = Query(0, ge=0, description="Number of tasks to skip"),
    limit: int = Query(20, ge=1, le=200, description="Maximum number of tasks to return"),
    completed: Optional[bool] = Query(None, description="Filter by completion status"),
    priority: Optional[str] = Query(None, description="Filter by priority: low, medium, or high"),
    due_before: Optional[datetime.date] = Query(None, description="Return tasks due on or before this date"),
    db: Session = Depends(database.get_db),
):
    query = db.query(models.Task)
    if completed is not None:
        query = query.filter(models.Task.completed == completed)
    if priority is not None:
        query = query.filter(models.Task.priority == priority)
    if due_before is not None:
        query = query.filter(models.Task.due_date <= due_before)
    return query.offset(skip).limit(limit).all()


# --- Get Task by ID ---
@router.get("/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(database.get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# --- Update Task ---
@router.put("/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, updated_task: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = updated_task.title
    task.description = updated_task.description
    task.priority = updated_task.priority
    task.due_date = updated_task.due_date
    db.commit()
    db.refresh(task)
    return task


# --- Mark Task Completed ---
@router.patch("/{task_id}/complete", response_model=schemas.Task)
def complete_task(task_id: int, db: Session = Depends(database.get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.completed = True
    db.commit()
    db.refresh(task)
    return task


# --- Delete Task ---
@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
