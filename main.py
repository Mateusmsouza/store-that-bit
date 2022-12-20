import logging
from logging.config import fileConfig

import uvicorn
from settings import app_settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.files import FILE_ROUTER


DEBUG_FILE_CONFIG = 'config/logging_debug.ini'
PROD_FILE_CONFIG = 'config/logging_prod.ini'
LOGGER = logging.getLogger(app_settings.app_logger_name)

app = FastAPI()
app.include_router(FILE_ROUTER)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def settup_logging():
    if app_settings.app_is_debug:
        fileConfig(DEBUG_FILE_CONFIG)
    else:
        fileConfig(PROD_FILE_CONFIG)

if __name__ == '__main__':
    settup_logging()
    LOGGER.info(f'starting server {app_settings.server_host} {app_settings.server_port}')
    uvicorn.run(
        app,
        host=app_settings.server_host,
        port=app_settings.server_port)
