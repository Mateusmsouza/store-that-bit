import logging

from settings import app_settings
from app.connections.oci_connection import OciConnection

LOGGER = logging.getLogger(app_settings.app_logger_name)


class StorageService:

    def upload_file(self, file, name):
        LOGGER.debug('uploading file to OCI')
        oci_connection = OciConnection()
        oci_connection.upload(file, name)
