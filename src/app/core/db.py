"""Database connection"""
from fastapi import Depends
from sqlmodel import Session, create_engine

from core.config import settings

engine = create_engine(settings.database_url, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

ActiveSession = Depends(get_session)
