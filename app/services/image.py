from fastapi import UploadFile, HTTPException

async def upload_new_image(file: UploadFile = None):
    if file == None:
        raise HTTPException(400, detail='Bad request, no file in your request')
    
    return {'message': 'hello from service upload_new_image()'}