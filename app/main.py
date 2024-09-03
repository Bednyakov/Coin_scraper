from fastapi import FastAPI, Query
from celery.result import AsyncResult
from .worker import create_task

app = FastAPI()

@app.get("/invoke_function/")
async def invoke_function(param1: str, param2: int):
    # Создаем задачу в Celery
    task = create_task.delay(param1, param2)
    return {"task_id": task.id}

@app.get("/task_status/{task_id}")
async def get_task_status(task_id: str):
    # Проверяем статус задачи
    task_result = AsyncResult(task_id)
    if task_result.state == 'SUCCESS':
        return {"task_id": task_id, "status": task_result.state, "result": task_result.result}
    return {"task_id": task_id, "status": task_result.state}


