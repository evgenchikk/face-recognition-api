import re

from fastapi import HTTPException, UploadFile


def fileValidator(file: UploadFile):
    if file == None:
        raise HTTPException(400, 'no file provided in your request')
    if file.content_type not in ['image/jpeg', 'image/png']:
        raise HTTPException(400, 'wrong file type, expected jpeg or png')
    if file.size > 2 * 1024 * 1024:
        raise HTTPException(400, 'file is too large, expected file < 2 MB')

def colorValidator(color: str):
    if not re.match(r'[0-9A-Fa-f]{3}|[0-9A-Fa-f]{6}', color):
        raise HTTPException(400,
                            'wrong color format, expected color in hex RGB format: <RRGGBB> or <RGB> (request example /1?color=f99)'
        )
