# import uvicorn
from fastapi import FastAPI, Depends
from dotenv import load_dotenv

from .routers import image
from .core import config


if not load_dotenv():
    print('No env variables are set')
    exit(1)

app = FastAPI()

app.include_router(image.router)

@app.get('/')
async def root():
    return {'message': 'See available methods on /docs'}
