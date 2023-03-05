from fastapi import UploadFile, Depends

from app.repository.image_repository import ImageRepository
from app.internal.faceplusplus import FacePlusPlusApi


class ImageService():
    def __init__(self, imageRepository: ImageRepository = Depends(ImageRepository), facePlusPlusApi: FacePlusPlusApi = Depends(FacePlusPlusApi)):
        self.imageRepository = imageRepository
        self.facePlusPlusApi = facePlusPlusApi

    async def upload_new_image(self, file: UploadFile = None):
        try:
            api_response = await self.facePlusPlusApi.upload(file)
            id = self.imageRepository.upload_image(file.filename, api_response)
        except Exception as e:
            return f'Internal error: {str(e)}'

        return id

    def get_image_with_colored_face(self, id: int, color: str):
        return ''
