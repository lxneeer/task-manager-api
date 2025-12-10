from fastapi import FastAPI
from typing import List

app = FastAPI(
    title="Task Manager API",
    description="API для управления задачами",
    version="1.0.0"
)


tasks_db = [
    {"id": 1, "title": "Изучить FastAPI", "completed": False},
    {"id": 2, "title": "Создать проект", "completed": True},
]

@app.get("/")
def home():
    return {"message": "Task Manager API работает!"}

@app.get("/tasks", response_model=List[dict])
def get_tasks():
    return tasks_db

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    return {"error": "Задача не найдена"}

@app.post("/tasks")
def create_task(title: str):
    new_id = max([task["id"] for task in tasks_db]) + 1 if tasks_db else 1
    new_task = {"id": new_id, "title": title, "completed": False}
    tasks_db.append(new_task)
    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, completed: bool):
    for task in tasks_db:
        if task["id"] == task_id:
            task["completed"] = completed
            return task
    return {"error": "Задача не найдена"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks_db):
        if task["id"] == task_id:
            deleted_task = tasks_db.pop(i)
            return {"message": "Задача удалена", "task": deleted_task}
    return {"error": "Задача не найдена"}
