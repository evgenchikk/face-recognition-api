from os import environ
from abc import ABC
from dotenv import load_dotenv


class Config(ABC):
    def __init__(self) -> None:
        self.POSTGRES_USERNAME = environ.get('POSTGRES_USERNAME') or 'postgres'
        self.POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD') or None
        self.POSTGRES_DB_NAME = environ.get('POSTGRES_DB_NAME') or 'aidiagnostic'
        self.POSTGRES_DB_HOST = environ.get('POSTGRES_DB_HOST') or 'localhost'
        self.POSTGRES_DB_PORT = environ.get('POSTGRES_DB_PORT') or '5432'

        self.FACE_PLUS_PLUS_API_KEY = environ.get('FACE_PLUS_PLUS_API_KEY') or None
        self.FACE_PLUS_PLUS_API_SECRET = environ.get('FACE_PLUS_PLUS_API_SECRET') or None
        self.FACE_PLUS_PLUS_API_URL = 'https://api-us.faceplusplus.com/facepp/v3/detect'

        self.LOCAL_IMAGES_CATALOG = 'uploads'

load_dotenv()

config = Config()
