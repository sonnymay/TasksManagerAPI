from __future__ import annotations

import datetime
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict

Priority = Literal["low", "medium", "high"]


class TaskBase(BaseModel):
        title: str
        description: str | None = None
        priority: Priority | None = None
        due_date: datetime.date | None = None


class TaskCreate(TaskBase):
        pass


class TaskUpdate(BaseModel):
        """All fields are optional so callers can do partial updates."""
        title: Optional[str] = None
        description: Optional[str] = None
        priority: Optional[Priority] = None
        due_date: Optional[datetime.date] = None
        completed: Optional[bool] = None


class Task(TaskBase):
        id: int
        completed: bool
        created_at: datetime.datetime
        updated_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)
