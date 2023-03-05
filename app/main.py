from fastapi import FastAPI

from app.routers import image_router


app = FastAPI()

app.include_router(image_router.router)

@app.get('/')
async def root():
    return {'message': 'See available methods on /docs'}
