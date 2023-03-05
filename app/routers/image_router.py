from fastapi import APIRouter, UploadFile, HTTPException, Response, Depends

from app.services.image_service import ImageService
from app.internal.faceplusplus import fileValidator


router = APIRouter(
    prefix='/image',
    tags=['image'],
)

@router.post('')
async def image_post(response: Response, file: UploadFile = None, imageService: ImageService = Depends(ImageService), fileValidator = Depends(fileValidator)):
    if file == None:
        response.status_code = 400
        return {'detail': 'no file provided in your request'}

    try:
        id = await imageService.upload_new_image(file)
        response.status_code = 201
    except Exception as e:
        response.status_code = 500
        return {'detail': str(e)}

    return {'id': id}

@router.get('/{id}')
async def image_get(id: int, color: str = None, imageService: ImageService = Depends(ImageService)):
    return {'data': imageService.get_image_with_colored_face(id, color)}

@router.put('/{id}')
async def image_put(id: int, file: UploadFile = None, imageService: ImageService = Depends(ImageService)):
    pass

@router.delete('/{id}')
async def image_delete(id: int, imageService: ImageService = Depends(ImageService)):
    pass
