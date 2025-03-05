import requests
from sqlalchemy.orm import Session

import models
import schemas

GEMINI_API_KEY = "AIzaSyC8nBqDEim0-DqTp1UqOKN445Fi6jIRRtwY"  # This is my API key (shohrukhdev@gmail.com) don't use it.
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"


def generate_project_tasks(project_name: str, location: str):
    prompt = f"List of key tasks for constructing a {project_name} in {location}."
    response = requests.post(
        GEMINI_URL,
        json={"contents": [{"parts": [{"text": prompt}]}]},
        params={"key": GEMINI_API_KEY}
    )

    if response.status_code == 200:
        tasks = response.json().get("candidates", [])[0].get("content", {}).get("parts", [])
        return [{"name": task, "status": "pending"} for task in tasks]
    return []


def create_project(db: Session, project: schemas.ProjectCreate):
    new_project = models.Project(
        project_name=project.project_name,
        location=project.location,
        status="processing"
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    tasks = generate_project_tasks(project.project_name, project.location)

    for task in tasks:
        db.add(models.Task(project_id=new_project.id, name=task["name"], status="pending"))
    db.commit()

    return new_project
