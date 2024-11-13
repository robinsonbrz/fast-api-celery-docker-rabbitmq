from celery import Celery

from core.config import settings

celery_app = Celery(__name__, broker=settings.RABBIT_URL, backend="rpc://")
print(settings.RABBIT_URL)

celery_app.conf.update(
    imports=['celery_src.celery_tasks'],
    broker_connection_retry_on_startup=True,
    task_track_started=True
)
