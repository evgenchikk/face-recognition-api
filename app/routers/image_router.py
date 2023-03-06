from fastapi import APIRouter, UploadFile, HTTPException, Response, Depends

from app.services.image_service import ImageService
from app.internal.validators import fileValidator, colorValidator


router = APIRouter(
    prefix='/image',
    tags=['image'],
)

@router.post('')
async def image_post(response: Response, file: UploadFile = None, image_service: ImageService = Depends(ImageService), fileValidator = Depends(fileValidator)):
    if file == None:
        response.status_code = 400
        return {'detail': 'no file provided in your request'}

    try:
        id = await image_service.upload_image(file)
    except Exception as e:
        response.status_code = 500
        return {'detail': str(e)}

    response.status_code = 201
    return {'id': id}

@router.get('/{id}')
async def image_get(response: Response, id: int, color: str = None, image_service: ImageService = Depends(ImageService), colorValidator = Depends(colorValidator)):
    try:
        image_service.get_image_with_colored_face(id, color)
    except Exception as e:
        response.status_code = 500
        return {'detail': f'{str(e)}'}

    response.status_code = 200
    return {'data': ''}

@router.put('/{id}')
async def image_put(id: int, file: UploadFile = None, image_service: ImageService = Depends(ImageService)):
    pass

@router.delete('/{id}')
async def image_delete(response: Response, id: int, image_service: ImageService = Depends(ImageService)):
    try:
        id = image_service.delete_image_by_id(id)
    except Exception as e:
        response.status_code = 500
        return {'detail': f'{str(e)}'}

    response.status_code = 200
    return {'id': id}
