from fastapi import APIRouter, UploadFile, Depends
from ..services import image as imageService

from ..core.config import Config, get_config

router = APIRouter(
    prefix='/image',
    tags=['image'],
    # responses={
    #     404: {'description': 'Not found'},
    #     500: {'desctiprion': 'Internal server error'},
    #     200: {'description': 'Ok'},
    # }
)

@router.post('')
async def image_post(file: UploadFile = None):
    return await imageService.upload_new_image(file)

@router.get('/{id}')
async def image_get(id: int, color: str | None = None, config: Config = Depends(get_config)):
    return {'message': f'hello from image_get: {id=}, {color=}, {config.FACE_PLUS_PLUS_API_KEY}'}

@router.put('/{id}')
async def image_put():
    pass

@router.delete('/{id}')
async def image_delete():
    pass