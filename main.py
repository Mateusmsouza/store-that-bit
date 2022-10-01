import logging

import uvicorn
from settings import app_settings
from fastapi import FastAPI

from app.routers.files import file_router

app = FastAPI()
app.include_router(file_router)

if __name__ == '__main__':
    logging.info('starting server')
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8000,
        debug=app_settings.app_is_debug)
