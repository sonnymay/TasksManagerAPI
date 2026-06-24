from __future__ import annotations

import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


Priority = Literal["low", "medium", "high"]


class TaskBase(BaseModel):
    title: str
    description: str | None = None
    priority: Priority | None = None
    due_date: datetime.date | None = None


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    completed: bool

    model_config = ConfigDict(from_attributes=True)
