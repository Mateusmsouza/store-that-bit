import logging
import traceback

from fastapi import APIRouter, File, UploadFile, HTTPException
from mongoengine import DoesNotExist

from app.services.storage_service import StorageService
from settings import app_settings


LOGGER = logging.getLogger(app_settings.app_logger_name)
FILE_ROUTER = APIRouter()

@FILE_ROUTER.post('/api/file/update', tags=['files'])
async def update_file(file_upload: UploadFile = File()):
    try:
        LOGGER.info('uploading file')
        file = await file_upload.read()
        if len(file) > app_settings.app_file_size_limit:
            raise BufferError
        uuid = StorageService().upload_file(
            file=file, name=file_upload.filename)
        return {
            "uuid": uuid
        }
    except BufferError:
        LOGGER.debug("file is too heavy")
        raise HTTPException(
            status_code=413,
            detail="file is too heavy.")
    except Exception:
        LOGGER.critical(traceback.format_exc())

@FILE_ROUTER.get('/api/file/{uuid}', tags=['files'])
async def get_file(uuid: str) -> dict:
    try:
        LOGGER.info('getting file url')
        return StorageService().get_file(uuid=uuid)
    except DoesNotExist:
        LOGGER.debug('file not found')
        raise HTTPException(status_code=404)

    except Exception:
        LOGGER.critical(traceback.format_exc())
