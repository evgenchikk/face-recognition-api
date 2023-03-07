from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import config


DATABASE_URL = f'postgresql+pg8000://{config.POSTGRES_USERNAME}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_DB_HOST}:{config.POSTGRES_DB_PORT}/{config.POSTGRES_DB_NAME}'
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

def get_session() -> Generator:
    try:
        yield SessionLocal()
    finally:
        SessionLocal.close_all()
