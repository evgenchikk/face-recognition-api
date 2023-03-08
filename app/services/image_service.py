import json
import uuid
from io import BytesIO

from fastapi import UploadFile, Depends

from sqlalchemy import exc

from app.repository.image_repository import ImageRepository
from app.repository.local_repository import LocalRepository
from app.internal.faceplusplus import FacePlusPlusApi
from app.internal.image_processing import ImageProcessor


class ImageService():
    def __init__(self,
                 image_repository: ImageRepository = Depends(ImageRepository),
                 local_repository: LocalRepository = Depends(LocalRepository),
                 face_plus_plus_api: FacePlusPlusApi = Depends(FacePlusPlusApi),
                 image_processor: ImageProcessor = Depends(ImageProcessor)):
        self.image_repository = image_repository
        self.local_repository = local_repository
        self.face_plus_plus_api = face_plus_plus_api
        self.image_processor = image_processor


    async def upload_image(self, file: UploadFile = None):
        try:
            file_binary = await file.read()
            filename = f'{uuid.uuid4()}.{file.filename.split(".")[-1]}'

            api_response = await self.face_plus_plus_api.upload(file_binary)
            await self.local_repository.save_file(filename=filename, file_binary=file_binary)
            id = await self.image_repository.save_image(filename=filename)
            await self.image_repository.save_api_response(api_response=json.dumps(api_response), image_id=id)
        except Exception as e:
            return f'Internal error: {str(e)}'

        return id


    async def get_image_with_colored_face(self, id: int, color: str) -> tuple:
        try:
            image = await self.image_repository.get_image_by_id(id=id)
            fpp_response = await self.image_repository.get_api_response_by_image_id(image_id=id)
        except Exception as e:
            return f'Internal error: {str(e)}'

        try:
            processed_binary = await self.image_processor.draw_rectangle(filename=image.filename,
                                                                         color=color,
                                                                         fpp_response=json.loads(fpp_response.fpp_response))
        except Exception as e:
            return f'Failed on drawing face rect: {str(e)}'

        result = BytesIO(processed_binary)
        result.seek(0)

        return result, str(image.filename).split('.')[-1]


    async def delete_image_by_id(self, id: int) -> int:
        try:
            await self.image_repository.delete_api_response_by_image_id(image_id=id)
            id = await self.image_repository.delete_image_by_id(id)
        except Exception as e:
            return f'Internal error: {str(e)}'

        return id


    async def replace_image_with_id(self, id: int, file: UploadFile = None):
        try:
            file_binary = await file.read()
            filename = f'{uuid.uuid4()}.{file.filename.split(".")[-1]}'

            api_response = await self.face_plus_plus_api.upload(file=file_binary)

            await self.local_repository.save_file(filename=filename, file_binary=file_binary)
            image_id = await self.image_repository.update_image_by_id(id=id, filename=filename)
            await self.image_repository.update_api_response_by_image_id(image_id=image_id, api_response=api_response)
        except Exception as e:
            return f'Internal error: {str(e)}'

        return image_id
