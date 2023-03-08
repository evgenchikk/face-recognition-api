import requests

from fastapi import UploadFile, HTTPException, Depends

from app.core.config import Config


class FacePlusPlusApi():
    def __init__(self, config: Config = Depends(Config)):
        self.api_key = config.FACE_PLUS_PLUS_API_KEY
        self.api_secret = config.FACE_PLUS_PLUS_API_SECRET
        self.api_url = config.FACE_PLUS_PLUS_API_URL


    async def upload(self, file: bytes):
        data = {
            'api_key': self.api_key,
            'api_secret': self.api_secret,
            'return_attributes': 'headpose',
        }
        files = {
            'image_file': file,
        }

        api_response = requests.post(
            url=self.api_url,
            data=data,
            files=files,
        )

        if not api_response.ok:
            raise HTTPException(500, f'problems with Face++ API: {api_response.json()}')
        return api_response.json()
