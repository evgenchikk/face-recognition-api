from fastapi import UploadFile, Depends

from app.repository.image_repository import ImageRepository
from app.internal.faceplusplus import FacePlusPlusApi


class ImageService():
    def __init__(self, image_repository: ImageRepository = Depends(ImageRepository), face_plus_plus_api: FacePlusPlusApi = Depends(FacePlusPlusApi)):
        self.image_repository = image_repository
        self.face_plus_plus_api = face_plus_plus_api

    async def upload_image(self, file: UploadFile = None):
        try:
            api_response = await self.face_plus_plus_api.upload(file)
            id = self.image_repository.upload_image(file.filename, api_response)
        except Exception as e:
            return f'Internal error: {str(e)}'

        return id

    def get_image_with_colored_face(self, id: int, color: str):
        return ''
