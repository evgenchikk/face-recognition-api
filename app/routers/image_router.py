from fastapi import APIRouter, UploadFile, HTTPException, Response, Depends
from fastapi.responses import StreamingResponse

from app.services.image_service import ImageService
from app.internal.validators import fileValidator, colorValidator


router = APIRouter(
    prefix='/image',
    tags=['image'],
)


# Принимает картинку, прогоняет ее через API [FacePlusPlus](https://www.faceplusplus.com/), и кладет результат в базу.
# Возвращает JSON `{‘id’: <id>}`
@router.post('')
async def image_post(response: Response,
                     file: UploadFile = None,
                     image_service: ImageService = Depends(ImageService),
                     fileValidator = Depends(fileValidator)):
    try:
        id = await image_service.upload_image(file)
    except Exception as e:
        raise HTTPException(500, detail=str(e))

    response.status_code = 201
    return {'id': id}


# Принимает id и параметр color – цвет, этим цветом отрисовывает на картинке лица,
# которые нашлись с помощью FacePlusPlus и возвращает в ответ отрисованную картинку
@router.get('/{id}')
async def image_get(id: int,
                    color: str = None,
                    image_service: ImageService = Depends(ImageService),
                    colorValidator = Depends(colorValidator)):
    try:
        file_bytes_iterator, extension = await image_service.get_image_with_colored_face(id, color)
    except Exception as e:
        raise HTTPException(500, detail=str(e))

    return StreamingResponse(file_bytes_iterator,
                             200,
                             headers={'Content-Disposition': f'attachment; filename=processed.{extension}'})


# Принимает картинку, меняет ее для записи с соответствующим id и прогоняет через FacePlusPlus
@router.put('/{id}')
async def image_put(response: Response,
                    id: int,
                    file: UploadFile = None,
                    image_service: ImageService = Depends(ImageService),
                    fileValidator = Depends(fileValidator)):
    try:
        id = await image_service.replace_image_with_id(id, file)
    except Exception as e:
        raise HTTPException(500, detail=str(e))

    response.status_code = 201
    return {'id': id}


# Удаляет картинку и запись с соответствующим id
@router.delete('/{id}')
async def image_delete(response: Response,
                       id: int, image_service:
                       ImageService = Depends(ImageService)):
    try:
        id = await image_service.delete_image_by_id(id)
    except Exception as e:
        raise HTTPException(500, detail=str(e))

    response.status_code = 200
    return {'id': id}
