import json

from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_session
from app.models.models import ImageModel, FppResponceModel


class ImageRepository():
    def __init__(self, db_session: Session = Depends(get_session)):
        self.db_session = db_session

    def upload_image(self, filename: str, api_response: dict):
        image = ImageModel(
            filename=filename,
        )

        try:
            self.db_session.add(image)
            self.db_session.commit()
            self.db_session.refresh(image)
        except Exception as e:
            raise Exception(e)

        fpp_response = FppResponceModel(
            fpp_response=json.dumps(api_response),
            image_id=image.id,
        )

        try:
            self.db_session.add(fpp_response)
            self.db_session.commit()
            self.db_session.refresh(fpp_response)
        except Exception as e:
            raise Exception(e)

        return image.id

