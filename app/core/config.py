from os import environ
from abc import ABC
from dotenv import load_dotenv


class Config(ABC):
    def __init__(self) -> None:
        self.POSTGRES_USERNAME = 'postgres'
        self.POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD') or None
        self.POSTGRES_DB_NAME = 'aidiagnostic'
        self.POSTGRES_DB_HOST = '164.92.246.254'
        self.POSTGRES_DB_PORT = '10230'

        self.FACE_PLUS_PLUS_API_KEY = environ.get('FACE_PLUS_PLUS_API_KEY') or None

if not load_dotenv():
    print('No env variables are set')
    exit(1) 

config = Config()

def get_config() -> Config:
    return config