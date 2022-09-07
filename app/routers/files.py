from fastapi import APIRouter, File, Form, UploadFile

file_router = APIRouter()

@file_router.post('/api/file/update', tags=['files'])
async def update_file(
    file: bytes = File()
):
    return {
        "file_size": len(file)
    }
