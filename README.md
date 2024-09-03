# Coin_scraper

## Запуск Celery Worker
Запустите Celery worker:
```
celery -A app.worker worker --loglevel=info
```

## Запуск FastAPI приложения
Запустите ваше FastAPI приложение (например, с помощью Uvicorn):
```
uvicorn app.main:app --reload
```


