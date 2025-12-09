
Task Manager API

# Task Manager API

Простой, но мощный REST API для управления задачами, построенный на FastAPI.


### Установка:
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

# Получить все задачи
curl http://localhost:8000/tasks

# Создать задачу
curl -X POST "http://localhost:8000/tasks?title=Изучить%20FastAPI"

# Обновить задачу
curl -X PUT "http://localhost:8000/tasks/1?completed=true"
