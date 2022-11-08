import logging

from settings import app_settings
from app.data.database import Database
from app.connections.oci_connection import OciConnection

LOGGER = logging.getLogger(app_settings.app_logger_name)


class StorageService:

    def upload_file(self, file, name):
        LOGGER.debug('uploading file to OCI')
        Database().save_file(
            filename=name,
            url=f'{app_settings.oci_bucket_public_url}/{name}'
        )
        oci_connection = OciConnection()
        oci_connection.upload(file, name)
