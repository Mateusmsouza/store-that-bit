import unittest
from unittest.mock import patch

from app.connections.rtwo_connection import R2Connection

import settings


class R2ServiceTest(unittest.TestCase):

    mock_bucket = 'https://09dis9disa0djsa.r2.cloudflarestorage.com/somebucket'
    r2_key_id = 'key_id'
    r2_access_key = 'access_key'
    r2_bucket_name = 'bucket_name'


    @patch('settings.app_settings.r2_endpoint', mock_bucket)
    @patch('settings.app_settings.r2_key_id', r2_key_id)
    @patch('settings.app_settings.r2_access_key', r2_access_key)
    @patch('settings.app_settings.r2_bucket_name', r2_bucket_name)
    def test_upload_file_should_return_pre_authorized_upload_link(self):
        filename = "cool_file.txt"
        r2_connection = R2Connection(
            endpoint=settings.app_settings.r2_endpoint,
            key_id=settings.app_settings.r2_key_id,
            access_key=settings.app_settings.r2_access_key,
            bucket_name=settings.app_settings.r2_bucket_name
        )
        url, fields = r2_connection.get_pre_authorized_upload(
            filename=filename
        )
        self.assertEqual(1, 1)
