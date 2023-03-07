import asyncio

from fastapi import Depends

from app.core.config import Config


class LocalRepository():
    def __init__(self, config: Config = Depends(Config)):
        self.upload_images_catalog = config.LOCAL_IMAGES_CATALOG

    async def save_file(file):
        pass

    async def get_file_by_name(filename: str) -> None:
        pass