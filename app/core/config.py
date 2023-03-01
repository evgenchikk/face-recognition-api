from os import environ
from abc import ABC

class Config(ABC):
    POSTGRES_USERNAME = 'postgres'
    POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD') or ''
    POSTGRES_DB_NAME = 'postgres'
    POSTGRES_DB_HOST = 'localhost'
    POSTGRES_DB_PORT = '5432'

    FACE_PLUS_PLUS_API_KEY = environ.get('FACE_PLUS_PLUS_API_KEY')

def get_config() -> Config:
    return Config()
