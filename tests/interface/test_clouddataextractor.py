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
        