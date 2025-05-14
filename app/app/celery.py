import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

celery_app = Celery('app')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

from celery.schedules import crontab

celery_app.conf.beat_schedule = {
    "check-notify-every-minute": {
        "task": "tg_app.tasks.check_and_notify",
        "schedule": crontab(minute="*"),
    }
}
