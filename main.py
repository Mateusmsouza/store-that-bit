from fastapi import FastAPI
from app.routers.files import file_router

app = FastAPI()
app.include_router(file_router)
