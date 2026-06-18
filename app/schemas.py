from pydantic import BaseModel, ConfigDict

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    completed: bool

    model_config = ConfigDict(from_attributes=True)
