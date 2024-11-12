import asyncio
from time import sleep
from datetime import datetime
from core.celery.celery  import celery_app


@celery_app.task
def send_mail_task(arg1, arg2):
    print(f"Envio de email processado assíncrono sem segurar a resposta da api: {arg1}, {arg2}")
    print(datetime.now())
    sleep(15)
    print("How I love God!!!!!!")
    print(datetime.now())
