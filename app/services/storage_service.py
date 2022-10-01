import logging

from app.connections.oci_connection import OciConnection

class StorageService:

    def upload_file(self, file):
        logging.debug('uploading file to OCI')
        oci_connection = OciConnection()
        oci_connection.upload(file)
