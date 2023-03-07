import math

import cv2
from fastapi import Depends

from app.core.config import Config


class ImageProcessor():
    def __init__(self, config: Config = Depends(Config)):
        self.local_images_catalog = config.LOCAL_IMAGES_CATALOG

    def draw_rectangle(self, filename: str, color: str, face_rectangle: dict, headpose: dict):
        img = cv2.imread(f'{self.images_catalog}/{filename}')
        pt1 = (face_rectangle['left'], face_rectangle['top'])
        pt2 = (int((face_rectangle['left']+face_rectangle['width']) * math.cos(math.radians(headpose['pitch_angle']))),
               int((face_rectangle['top']+face_rectangle['height']) * math.cos(math.radians(headpose['pitch_angle'])))
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
        cv2.imshow('result', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
