from app.celery import celery_app
from django.utils import timezone
from config import settings
from .models import Task
import requests


@celery_app.task
def check_and_notify():
    now = timezone.now()
    tasks = Task.objects.filter(notice_time_date__lte=now, notified=False)
    for task in tasks:
        result = send_via_bot_api(task.user_id, task.message)
        if result:
            task.notified = True
            task.save()


def send_via_bot_api(user_id: int, message: str):
    url = f'http://{settings.aiohttp_url}notify/'
    try:
        response = requests.post(
            url,
            json={"user_id": user_id, "message": message},
            timeout=5
        )
        response.raise_for_status()
        if response.status_code == 200:
            return True
    except Exception as e:
        print(f"Ошибка при отправке в бот: {e}")
        return False
