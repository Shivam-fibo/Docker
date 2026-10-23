
import utils.session
from fastapi import FastAPI

app = FastAPI()

tasks = [
    {"id": 1, "title": "Learn Python", "completed": False},
    {"id": 2, "title": "Learn Docker", "completed": False},
]


@app.get("/")
def home():
    return {"message": "Python backend is running"}


@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}


@app.post("/tasks")
def create_task(title: str):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False,
    }

    tasks.append(task)
    return task
