import logging

from oci.config import validate_config
from oci.object_storage import ObjectStorageClient
from oci.object_storage.models import CopyObjectDetails

from settings import app_settings


class OciConnection:

    def __init__(self) -> None:
        self.config = {
            "user": app_settings.oci_user_ocid,
            "key_file": app_settings.oci_keyfile_path,
            "fingerprint": app_settings.oci_fingerprint,
            "tenancy": app_settings.oci_tenancy,
            "region": app_settings.oci_region
        }

        validate_config(self.config)
        logging.debug('config OCI validated')
    
    def upload(self, file):
        object_storage = ObjectStorageClient(self.config)
        CopyObjectDetails()
        object_storage.put_object(
            bucket_name=app_settings.oci_bucket_name,
            namespace_name=app_settings.oci_bucket_namespace,
            object_name='teste',
            put_object_body=file
        )
