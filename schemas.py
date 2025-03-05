from pydantic import BaseModel
from typing import List, Optional


class TaskBase(BaseModel):
    name: str
    status: str = "pending"

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    project_name: str
    location: str

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    status: str
    tasks: List[Task] = []

    class Config:
        orm_mode = True
