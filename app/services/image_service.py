from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session

async def upload_new_image(file: UploadFile = None, db_session: Session = None):
    if file == None:
        raise HTTPException(400, detail='Bad request, no file in your request')
    if db_session == None:
        raise HTTPException(500, detail='Internal server error, no connection to the database')

    return {'message': 'hello from service upload_new_image()'}
