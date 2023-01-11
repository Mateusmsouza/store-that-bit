import logging
from datetime import datetime

from settings import app_settings
from app.data.database import Database
from app.connections.oci_connection import OciConnection

LOGGER = logging.getLogger(app_settings.app_logger_name)


class StorageService:


    def upload_file(self, file, name) -> str:
        LOGGER.debug('uploading file to OCI')
        name, extenstion = name.split('.')
        filename = f'{name}{datetime.now().strftime("%d-%m-%Y_%H_%M_%S")}.{extenstion}'
        public_url = f'{app_settings.oci_bucket_public_url}/{filename}'
        file_saved = Database().save_file(
            filename=filename,
            url=public_url
        )
        if app_settings.app_is_debug is not True:
            oci_connection = OciConnection()
            oci_connection.upload(file, filename)

        return str(file_saved.id)

    def get_file(self, uuid: str) -> str:
        LOGGER.debug(f'getting {uuid}')
        file = Database().get_file_url(uuid=uuid)
        return file.file_url
