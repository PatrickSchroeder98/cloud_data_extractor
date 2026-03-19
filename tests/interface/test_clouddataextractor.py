import unittest
from unittest.mock import patch, MagicMock
from src.interface import clouddataextractor
from src.interface.clouddataextractor import CloudDataExtractor


class TestCloudDataExtractor(unittest.TestCase):
    """Class with tests of the CloudDataExtractor."""

    def test_init(self):
        """Method tests the initialization of a class"""
        cde = CloudDataExtractor()
        firestore_connection = None

        self.assertEqual(cde.get_firestore_connection() ,firestore_connection)

        del cde

    @patch("src.interface.clouddataextractor.FirestoreConnection")
    @patch("src.interface.clouddataextractor.Log")
    def test_set_firestore_connection(self, mock_log_class, mock_fs_conn):
        mock_log_class.return_value = MagicMock()

        extractor = CloudDataExtractor()

        extractor.set_firestore_connection("path.json", "emails")

        mock_fs_conn.assert_called_once_with("path.json", "emails")

        del extractor

    @patch("src.interface.clouddataextractor.FirestoreConnection")
    @patch("src.interface.clouddataextractor.Log")
    def test_get_firestore_connection(self, mock_log_class, mock_fs_conn):
        mock_log_class.return_value = MagicMock()

        extractor = CloudDataExtractor()

        extractor.set_firestore_connection("path.json", "emails")

        result = extractor.get_firestore_connection()

        assert result is not None

        del extractor

    @patch("src.interface.clouddataextractor.Log")
    def test_certificate_credentials_success(self, mock_log_class):
        mock_log_class.return_value = MagicMock()

        extractor = CloudDataExtractor()

        mock_fs = MagicMock()
        mock_fs.certificate_credentials.return_value = True
        mock_fs.get_credentials.return_value = "fake_credentials"

        extractor._CloudDataExtractor__firestore_connection = mock_fs

        result = extractor.certificate_credentials()

        assert result == "fake_credentials"

        del extractor

    @patch("src.interface.clouddataextractor.Log")
    @patch("src.interface.clouddataextractor.CredentialsError")
    def test_certificate_credentials_failure(self, mock_credentials_error, mock_log_class):
        mock_log = MagicMock()
        mock_log_class.return_value = mock_log

        mock_exception = MagicMock()
        mock_exception.get_message.return_value = "Credential error"
        mock_exception.get_code.return_value = "401"

        mock_credentials_error.return_value = mock_exception

        extractor = CloudDataExtractor()

        mock_fs = MagicMock()
        mock_fs.certificate_credentials.return_value = False

        extractor._CloudDataExtractor__firestore_connection = mock_fs

        result = extractor.certificate_credentials()

        assert result is None

        mock_log.error.assert_any_call("Credential error")
        mock_log.error.assert_any_call("Error code: 401")

        del extractor

    @patch("src.interface.clouddataextractor.Log")
    def test_initialize_app_calls_firestore_connection(self, mock_log_class):
        mock_log_class.return_value = MagicMock()

        extractor = CloudDataExtractor()

        mock_fs = MagicMock()
        extractor._CloudDataExtractor__firestore_connection = mock_fs

        extractor.initialize_app("fake_credentials")

        mock_fs.initialize_firestore.assert_called_once_with("fake_credentials")

        del extractor

    @patch("src.interface.clouddataextractor.Log")
    def test_db_client_success(self, mock_log_class):
        mock_log_class.return_value = MagicMock()

        extractor = CloudDataExtractor()

        mock_fs = MagicMock()
        mock_fs.db_client.return_value = True
        mock_fs.get_db.return_value = "fake_db"

        extractor._CloudDataExtractor__firestore_connection = mock_fs

        result = extractor.db_client()

        assert result == "fake_db"

        mock_fs.db_client.assert_called_once()
        mock_fs.get_db.assert_called_once()

        del extractor

    @patch("src.interface.clouddataextractor.Log")
    @patch("src.interface.clouddataextractor.DBError")
    def test_db_client_failure(self, mock_db_error, mock_log_class):
        mock_log = MagicMock()
        mock_log_class.return_value = mock_log

        mock_exception = MagicMock()
        mock_exception.get_message.return_value = "DB connection error."
        mock_exception.get_code.return_value = "DB_CONNECTION_ERROR_002"

        mock_db_error.return_value = mock_exception

        extractor = CloudDataExtractor()

        mock_fs = MagicMock()
        mock_fs.db_client.return_value = False

        extractor._CloudDataExtractor__firestore_connection = mock_fs

        result = extractor.db_client()

        assert result is None

        mock_log.error.assert_any_call("DB connection error.")
        mock_log.error.assert_any_call("Error code: DB_CONNECTION_ERROR_002")

        del extractor

    @patch("src.interface.clouddataextractor.Log")
    def test_db_get_collection_success(self, mock_log_class):
        mock_log_class.return_value = MagicMock()

        extractor = CloudDataExtractor()

        mock_fs = MagicMock()
        mock_fs.get_results.return_value = ["doc1", "doc2"]

        extractor._CloudDataExtractor__firestore_connection = mock_fs

        result = extractor.db_get_collection()

        assert result == ["doc1", "doc2"]
        mock_fs.get_results.assert_called_once()

        del extractor

    @patch("src.interface.clouddataextractor.Log")
    def test_db_get_collection_no_connection(self, mock_log_class):
        mock_log_class.return_value = MagicMock()

        extractor = CloudDataExtractor()

        result = extractor.db_get_collection()

        assert result is None

        del extractor
        