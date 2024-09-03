from celery import Celery
import requests

# Настройка брокера RabbitMQ
celery_app = Celery('tasks', broker='pyamqp://guest@localhost//')

@celery_app.task
def create_task(param1: str, param2: int):
    # Вызов Yandex Cloud Functions
    function_url = "https://functions.yandexcloud.net/<your-function-id>"
    response = requests.post(function_url, json={"param1": param1, "param2": param2})
    return response.json()

