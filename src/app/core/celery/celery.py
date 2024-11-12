from celery import Celery

from core.config import settings

celery_app = Celery(__name__, broker=settings.RABBIT_URL, backend="rpc://")

celery_app.conf.update(
    imports=['core.celery.celery_tasks'],
    broker_connection_retry_on_startup=True,
    task_track_started=True
)
