from fastapi import APIRouter
from core.db import ActiveSession
from sqlmodel import Session

from core.celery.celery_tasks import send_mail_task

router = APIRouter()

@router.get("/", )
async def health_check():
    data = {"health check":"ok"}
    return data

# Test database connection
@router.get("/test-db")
async def test_db_connection(*, session: Session = ActiveSession):
    try:
        result = session.execute("SELECT 1")
        return {"status": "Connected", "result": result.scalar()}
    except Exception as e:
        return {"status": "Connection failed", "error": str(e)}
    
@router.get("/send-email")
async def send_email(*, session: Session = ActiveSession):
    # Submitting a task
    send_mail_task.apply_async(args=("parametro-01", "parametro-02"))
    us = {"email":"sent"}
    return us
