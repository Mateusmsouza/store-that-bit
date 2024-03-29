from datetime import datetime, timedelta


from settings import app_settings
from mongoengine import connect
from app.data.file_model import FileStored


class Database:

    def __init__(self) -> None:
        self.connection = connect(
            db=app_settings.oci_database_name,
            host=app_settings.oci_database_connection_string,
        )

    def save_file(self, filename, url):
        file_saved = FileStored(
            filename=filename,
            file_url=url,
            created_at=datetime.now()
        )
        file_saved.save()
        return file_saved
    
    def get_file_url(self, uuid: str) -> FileStored:
        file: FileStored = FileStored.objects.get(id=uuid)
        return file
