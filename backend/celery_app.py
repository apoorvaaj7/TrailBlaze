from celery import Celery
from celery.schedules import crontab

celery = Celery(
    "trekking",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery.conf.update(
    timezone="Asia/Kolkata",
    broker_connection_retry_on_startup=True
)

celery.conf.beat_schedule = {

    "daily-reminder": {
        "task": "tasks.daily_reminder",
        "schedule": crontab(hour=8, minute=0)
    },

    "monthly-report": {
        "task": "tasks.monthly_report",
        "schedule": crontab(day_of_month=1, hour=9, minute=0)
    }

}

import tasks