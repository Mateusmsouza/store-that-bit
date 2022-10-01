import traceback

from fastapi import APIRouter, File, UploadFile

from app.services.storage_service import StorageService

file_router = APIRouter()

@file_router.post('/api/file/update', tags=['files'])
async def update_file(file_upload: UploadFile = File()):
    try:
        file = await file_upload.read()
        StorageService().upload_file(
            file
        )
        return {
            "file_size": len(file)
        }
    except Exception:
        print(traceback.format_exc())
