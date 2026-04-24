import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Adicionar src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import get_access_token, download_onedrive_file

class TestMain(unittest.TestCase):

    @patch('main.ConfidentialClientApplication')
    def test_get_access_token_success(self, mock_app):
        mock_app.return_value.acquire_token_for_client.return_value = {'access_token': 'fake_token'}
        with patch.dict(os.environ, {'CLIENT_ID': 'test', 'CLIENT_SECRET': 'test', 'TENANT_ID': 'test'}):
            token = get_access_token()
            self.assertEqual(token, 'fake_token')

    @patch('main.requests.get')
    def test_download_onedrive_file_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b'fake_data'
        mock_get.return_value = mock_response

        data = download_onedrive_file('test/path', 'fake_token')
        self.assertEqual(data, b'fake_data')

if __name__ == '__main__':
    unittest.main()