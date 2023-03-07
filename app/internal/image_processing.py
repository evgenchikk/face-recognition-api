import math

import cv2
from fastapi import Depends

from app.core.config import Config


class ImageProcessor():
    def __init__(self, config: Config = Depends(Config)):
        self.local_images_catalog = config.LOCAL_IMAGES_CATALOG


    async def draw_rectangle(self, filename: str, color: str, fpp_response: dict) -> bytes:
        img = cv2.imread(f'{self.local_images_catalog}/{filename}')

        for i in range (fpp_response['face_num']):
            pt1 = (fpp_response['faces'][i]['face_rectangle']['left'],
                   fpp_response['faces'][i]['face_rectangle']['top'])

            pt2 = (int((fpp_response['faces'][i]['face_rectangle']['left']+fpp_response['faces'][i]['face_rectangle']['width']) * math.cos(math.radians(fpp_response['faces'][i]['attributes']['headpose']['pitch_angle']))),
                   int((fpp_response['faces'][i]['face_rectangle']['top']+fpp_response['faces'][i]['face_rectangle']['height']) * math.cos(math.radians(fpp_response['faces'][i]['attributes']['headpose']['pitch_angle'])))
            )

            bgr = ''
            if len(color) == 6:
                bgr = (
                    int(f'0x{color[5]}{color[4]}', 0),
                    int(f'0x{color[3]}{color[2]}', 0),
                    int(f'0x{color[1]}{color[0]}', 0),
                )
            else:
                bgr = (
                    int(f'0x{color[2]}{color[2]}', 0),
                    int(f'0x{color[1]}{color[1]}', 0),
                    int(f'0x{color[0]}{color[0]}', 0),
                )

            cv2.rectangle(img, pt1, pt2, bgr, 3)

        img_buf = cv2.imencode(f'.{filename.split(".")[-1]}', img)[1]
        return img_buf.tobytes()
