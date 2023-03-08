import json

from fastapi import Depends

from sqlalchemy.orm import Session
from sqlalchemy import exc

from app.database.database import get_session
from app.models.models import ImageModel, FppResponseModel


class ImageRepository():
    def __init__(self, db_session: Session = Depends(get_session)):
        self.db_session = db_session


    # async def upload_image(self, filename: str, api_response: dict) -> int:
    #     image = ImageModel(
    #         filename=filename,
    #     )

    #     self.db_session.add(image)
    #     self.db_session.commit()
    #     self.db_session.refresh(image)

    #     fpp_response = FppResponseModel(
    #         fpp_response=json.dumps(api_response),
    #         image_id=image.id,
    #     )

    #     self.db_session.add(fpp_response)
    #     self.db_session.commit()
    #     self.db_session.refresh(fpp_response)

    #     return image.id


    # async def replace_fpp_response(self, api_response: dict, image_id: int) -> int:
    #     fpp_response = self.get_fpp_response_by_image_id(image_id)
    #     fpp_response.fpp_response = api_response

    #     self.db_session.add(fpp_response)
    #     self.db_session.commit()
    #     self.db_session.refresh(fpp_response)

    #     return fpp_response.id


    # def get_image_by_id(self, id: int) -> ImageModel:
    #     image = self.db_session.get(ImageModel, id)
    #     if not image:
    #         raise exc.NoResultFound()
    #     return image


    # def get_fpp_response_by_image_id(self, id) -> FppResponseModel:
    #     fpp_response = self.db_session.query(FppResponseModel).filter(FppResponseModel.image_id == id).one()
    #     if not fpp_response:
    #         raise exc.NoResultFound()
    #     return fpp_response


    # async def delete_image_by_id(self, id: int) -> int:
    #     image = self.db_session.get(ImageModel, id)
    #     if not image:
    #         raise exc.NoResultFound()

    #     fpp_response = self.get_fpp_response_by_image_id(image.id)
    #     if not fpp_response:
    #         raise exc.NoResultFound()

    #     self.db_session.delete(image)
    #     self.db_session.delete(fpp_response)
    #     self.db_session.commit()

    #     return image.id


    # async def replace_with_new_file(self, id: int, filename: str) -> int:
    #     image = self.db_session.get(ImageModel, id)
    #     if not image:
    #         raise exc.NoResultFound()

    #     image.filename = filename
    #     self.db_session.add(image)
    #     self.db_session.commit()
    #     self.db_session.refresh(image)

    #     return image.id


# #############################################


    async def save_image(self, filename: str) -> int:
        image = ImageModel(
            filename=filename,
        )

        self.db_session.add(image)
        self.db_session.commit()
        self.db_session.refresh(image)

        return image.id


    async def get_image_by_id(self, id: int) -> ImageModel:
        image = self.db_session.get(ImageModel, id)

        return image


    async def update_image_by_id(self, id: int, filename: str) -> int:
        image = self.db_session.get(ImageModel, id)

        image.filename = filename

        self.db_session.add(image)
        self.db_session.commit()
        self.db_session.refresh(image)

        return image.id


    async def delete_image_by_id(self, id: int) -> int:
        image = self.db_session.get(ImageModel, id)

        self.db_session.delete(image)
        self.db_session.commit()

        return image.id


    async def save_api_response(self, api_response: str, image_id: int) -> int:
        fpp_response = FppResponseModel(
            fpp_response=api_response,
            image_id=image_id,
        )

        self.db_session.add(fpp_response)
        self.db_session.commit()
        self.db_session.refresh(fpp_response)

        return fpp_response.id


    async def get_api_response_by_image_id(self, image_id: int) -> FppResponseModel:
        fpp_response = self.db_session.query(FppResponseModel).filter(FppResponseModel.image_id == image_id).one()

        return fpp_response


    async def update_api_response_by_image_id(self, image_id: int, api_response: str) -> int:
        fpp_response = self.db_session.query(FppResponseModel).filter(FppResponseModel.image_id == image_id).one()

        fpp_response.fpp_response = api_response

        self.db_session.add(fpp_response)
        self.db_session.commit()
        self.db_session.refresh(fpp_response)

        return fpp_response.id


    async def delete_api_response_by_image_id(self, image_id: int) -> int:
        fpp_response = self.db_session.query(FppResponseModel).filter(FppResponseModel.image_id == image_id).one()

        self.db_session.delete(fpp_response)
        self.db_session.commit()

        return fpp_response.id
