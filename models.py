from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Project(Base):
    """Table for projects entity."""
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, index=True)
    location = Column(String, index=True)
    status = Column(String, default="processing")

    tasks = relationship("Task", back_populates="project")




class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    name = Column(String, index=True)
    status = Column(String, default="pending")

    project = relationship("Project", back_populates="tasks")
