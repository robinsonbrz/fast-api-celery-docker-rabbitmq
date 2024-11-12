"""Database connection"""
from fastapi import Depends
from sqlmodel import Session, create_engine

from core.config import settings, DBOption

if settings.DB_ENGINE == DBOption.SQLITE:
    DATABASE_URI = settings.SQLITE_URI
    DATABASE_PREFIX = settings.SQLITE_SYNC_PREFIX
    DATABASE_URL = f"{DATABASE_PREFIX}{DATABASE_URI}"
if settings.DB_ENGINE == DBOption.POSTGRES:
    DATABASE_URI = settings.POSTGRES_URI
    DATABASE_PREFIX = settings.POSTGRES_SYNC_PREFIX
    DATABASE_URL = f"{DATABASE_PREFIX}{DATABASE_URI}"


engine = create_engine(DATABASE_URL , echo=True)

def get_session():
    with Session(engine) as session:
        yield session

ActiveSession = Depends(get_session)
