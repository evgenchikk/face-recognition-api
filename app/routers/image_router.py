from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.orm import Session

from app.services import image_service
from app.models import models
from app.core.config import Config, get_config
from app.db.db import get_db

router = APIRouter(
    prefix='/image',
    tags=['image'],
    dependencies=[Depends(get_config), Depends(get_db)]
)

@router.post('')
async def image_post(file: UploadFile = None, db_session: Session = Depends(get_db)):
    return await image_service.upload_new_image(file)

@router.get('/{id}')
async def image_get(id: int, color: str = None, config: Config = Depends(get_config), db_session: Session = Depends(get_db)):
    # t = db_session.query(models.Images)
    # return {'data': t}
    return {'data': f'{config.POSTGRES_PASSWORD}'}

@router.put('/{id}')
async def image_put():
    pass

@router.delete('/{id}')
async def image_delete():
    pass
