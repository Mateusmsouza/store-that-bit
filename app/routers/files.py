import traceback

from fastapi import APIRouter, File, UploadFile

file_router = APIRouter()

@file_router.post('/api/file/update', tags=['files'])
async def update_file(file_upload: UploadFile = File()):
    try:
        file = await file_upload.read()
        return {
            "file_size": len(file)
        }
    except Exception:
        print(traceback.format_exc())
