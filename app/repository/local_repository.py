import os

from fastapi import Depends

from app.core.config import Config


class LocalRepository():
    def __init__(self, config: Config = Depends(Config)):
        self.upload_images_catalog = config.LOCAL_IMAGES_CATALOG


    async def save_file(self, filename: str, file_binary: bytes) -> bool:
        try:
            os.makedirs(name=os.path.join(os.getcwd(), self.upload_images_catalog),
                        mode=0o755,
                        exist_ok=True)
        except Exception as e:
            return False

        with open(os.path.join(os.getcwd(), self.upload_images_catalog, filename), 'wb') as file:
            file.write(file_binary)


    async def get_file_by_name(filename: str) -> None:
        pass


    async def delete_file_by_name(self, filename: str) -> bool:
        try:
            os.remove(os.path.join(os.getcwd(), self.upload_images_catalog, filename))
        except Exception as e:
            return False

        return True
