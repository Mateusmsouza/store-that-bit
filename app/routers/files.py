import logging
import traceback

from fastapi import APIRouter, File, UploadFile

from app.services.storage_service import StorageService
from settings import app_settings


LOGGER = logging.getLogger(app_settings.app_logger_name)
FILE_ROUTER = APIRouter()

@FILE_ROUTER.post('/api/file/update', tags=['files'])
async def update_file(file_upload: UploadFile = File()):
    try:
        LOGGER.info('uploading file')
        file = await file_upload.read()
        StorageService().upload_file(
            file=file, name=file_upload.filename)
        return {
            "file_size": len(file)
        }
    except Exception:
        print(traceback.format_exc())
