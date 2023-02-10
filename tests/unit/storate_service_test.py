import unittest
from unittest.mock import patch

from app.services.storage_service import StorageService
from app.data.database import Database
from app.data.file_model import FileStored
from app.connections.oci_connection import OciConnection
from datetime import datetime

import settings


class StorageServiceTest(unittest.TestCase):

    mock_bucket = 'publicbucketurl'

    @patch('settings.app_settings.oci_bucket_public_url', mock_bucket)
    @patch.object(Database, 'save_file')
    @patch.object(OciConnection, 'upload')
    @patch.object(OciConnection, '__init__')
    def test_upload_file_should_return_public_url(self, mock_oci_init, mock_oci, mock_database):
        file_name = 'filename.txt'
        uuid = 'anyfileuuid'
        mock_database.return_value = FileStored(
            id=uuid,
            filename=file_name,
            file_url='any',
            created_at=datetime.now())

        mock_oci.return_value = None
        mock_oci_init.return_value = None

        storage_service = StorageService()
        file_url = storage_service.upload_file(None, file_name)
        self.assertEqual(file_url, uuid)
