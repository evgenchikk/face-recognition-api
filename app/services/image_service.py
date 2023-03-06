import json

from fastapi import UploadFile, Depends

from sqlalchemy import exc

from app.repository.image_repository import ImageRepository
from app.internal.faceplusplus import FacePlusPlusApi
from app.internal.image_processing import ImageProcessor


class ImageService():
    def __init__(self, image_repository: ImageRepository = Depends(ImageRepository), face_plus_plus_api: FacePlusPlusApi = Depends(FacePlusPlusApi), image_processor: ImageProcessor = Depends(ImageProcessor)):
        self.image_repository = image_repository
        self.face_plus_plus_api = face_plus_plus_api
        self.image_processor = image_processor

    async def upload_image(self, file: UploadFile = None):
        try:
            api_response = await self.face_plus_plus_api.upload(file)
            id = self.image_repository.upload_image(file.filename, api_response)
        except Exception as e:
            return f'Internal error: {str(e)}'

        return id

    def get_image_with_colored_face(self, id: int, color: str):
        try:
            image = self.image_repository.get_image_by_id(id)
            fpp_response = json.loads(self.image_repository.get_fpp_response_by_image_id(id).fpp_response)
        except exc.NoResultFound as e:
            raise Exception(f'Internal error: no result found with requestes id ({id})')
        except Exception as e:
            raise Exception(f'Internal error: {str(e)}')

        for i in range (fpp_response['face_num']):
            try:
                self.image_processor.draw_rectangle(filename=image.filename,
                                                    color=color,
                                                    face_rectangle=fpp_response['faces'][i]['face_rectangle'],
                                                    headpose=fpp_response['faces'][i]['attributes']['headpose'],
                )
            except Exception as e:
                return f'Internal error: {str(e)}'
        return ''

    def delete_image_by_id(self, id: int) -> int:
        try:
            id = self.image_repository.delete_image_by_id(id)
        except exc.NoResultFound as e:
            raise Exception(f'Internal error: no result found with requestes id ({id})')
        except Exception as e:
            raise Exception(f'Internal error: {str(e)}')

        return id
