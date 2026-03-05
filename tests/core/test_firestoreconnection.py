import pytest
import unittest
from unittest.mock import patch, MagicMock
from src.core.firestoreconnection import FirestoreConnection
from src.core.log import Log


class TestFirestoreConnection(unittest.TestCase):
    """Class with tests of the FirestoreConnection."""

    def test_init(self):
        """Method tests the initialization of a class"""
        firestore_connection = FirestoreConnection("example_path", "example_collection")

        path = "example_path"
        credentials = None
        db = None
        collection = "example_collection"
        results = None

        self.assertEqual(firestore_connection.get_path(), path)
        self.assertEqual(firestore_connection.get_credentials(), credentials)
        self.assertEqual(firestore_connection.get_db(), db)
        self.assertEqual(firestore_connection.get_collection_name(), collection)
        self.assertEqual(firestore_connection.get_results(), results)

        del firestore_connection

    def test_set_path(self):
        """Method tests the setting the path of firestore connection."""
        firestore_connection = FirestoreConnection("example_path", "example_collection")
        path = "example_path_test"

        firestore_connection.set_path(path)
        self.assertEqual(firestore_connection.get_path(), path)

        del firestore_connection

    def test_get_path(self):
        """Method tests the getting the path of firestore connection."""
        firestore_connection = FirestoreConnection("example_path", "example_collection")
        path = "example_path"

        self.assertEqual(firestore_connection.get_path(), path)

        del firestore_connection

    def test_set_credentials(self):
        """Method tests the setting the credentials of firestore connection."""
        firestore_connection = FirestoreConnection("example_path", "example_collection")
        credentials = "Example Credentials"

        firestore_connection.set_credentials(credentials)
        self.assertEqual(firestore_connection.get_credentials(), credentials)

        del firestore_connection

    def test_get_credentials(self):
        """Method tests the getting the credentials of firestore connection."""
        firestore_connection = FirestoreConnection("example_path", "example_collection")

        self.assertEqual(firestore_connection.get_credentials(), None)

        del firestore_connection

    def test_set_db(self):
        """Method tests the setting the db attribute."""
        firestore_connection = FirestoreConnection("example_path", "example_collection")
        db = "Example DB"

        firestore_connection.set_db(db)
        self.assertEqual(firestore_connection.get_db(), db)

        del firestore_connection

    def test_get_db(self):
        """Method tests the getting the db attribute."""
        firestore_connection = FirestoreConnection("example_path", "example_collection")

        self.assertEqual(firestore_connection.get_db(), None)

        del firestore_connection

    def test_set_collection(self):
        """Method tests the setting the collection attribute."""
        firestore_connection = FirestoreConnection("example_path", "example_collection")
        collection = "example_collection_test"

        firestore_connection.set_collection_name(collection)
        self.assertEqual(firestore_connection.get_collection_name(), collection)

        del firestore_connection

    def test_get_collection(self):
        """Method tests the getting the collection attribute."""
        firestore_connection = FirestoreConnection("example_path", "example_collection")

        self.assertEqual(firestore_connection.get_collection_name(), "example_collection")

        del firestore_connection

    def test_set_results(self):
        """Method tests the setting the results attribute."""
        firestore_connection = FirestoreConnection("example_path", "example_collection")
        results = "Example Results"

        firestore_connection.set_results(results)
        self.assertEqual(firestore_connection.get_results(), results)

        del firestore_connection

    def test_get_results(self):
        """Method tests the getting the results attribute."""
        firestore_connection = FirestoreConnection("example_path", "example_collection")

        self.assertEqual(firestore_connection.get_results(), None)

        del firestore_connection

    @patch("src.core.firestoreconnection.credentials.Certificate")
    @patch("src.core.firestoreconnection.Log")
    def test_certificate_credentials_success(self, mock_log_class, mock_certificate):
        """Method tests the certificate credentials method success route."""
        mock_log = MagicMock()
        mock_log_class.return_value = mock_log

        mock_certificate.return_value = MagicMock()

        conn = FirestoreConnection("fake/path.json", "test_collection")

        result = conn.certificate_credentials()

        assert result is True
        mock_certificate.assert_called_once_with("fake/path.json")
        mock_log.info.assert_called_once_with("File with credentials loaded successfully!")

        del conn

    @patch("src.core.firestoreconnection.credentials.Certificate")
    @patch("src.core.firestoreconnection.Log")
    def test_certificate_credentials_file_not_found(self, mock_log_class, mock_certificate):
        """Method tests the certificate credentials method when it raises FileNotFoundError exception."""
        mock_log = MagicMock()
        mock_log_class.return_value = mock_log

        mock_certificate.side_effect = FileNotFoundError

        conn = FirestoreConnection("fake/path.json", "test_collection")

        result = conn.certificate_credentials()

        assert result is False
        mock_log.error.assert_called_once_with("File with credentials not found!")

        del conn

    @patch("src.core.firestoreconnection.credentials.Certificate")
    @patch("src.core.firestoreconnection.Log")
    def test_certificate_credentials_permission_error(self, mock_log_class, mock_certificate):
        """Method tests the certificate credentials method when it raises PermissionError exception."""
        mock_log = MagicMock()
        mock_log_class.return_value = mock_log

        mock_certificate.side_effect = PermissionError

        conn = FirestoreConnection("fake/path.json", "test_collection")

        result = conn.certificate_credentials()

        assert result is False
        mock_log.error.assert_called_once_with(
            "File with credentials returned PermissionError!"
        )

        del conn

    @patch("src.core.firestoreconnection.firebase_admin.initialize_app")
    @patch("src.core.firestoreconnection.Log")
    def test_initialize_firestore_success(self, mock_log_class, mock_initialize):
        """Method tests the initialization method success route."""
        mock_log = MagicMock()
        mock_log_class.return_value = mock_log

        conn = FirestoreConnection("fake/path.json", "test_collection")

        fake_cred = MagicMock()

        conn.initialize_firestore(fake_cred)

        mock_initialize.assert_called_once_with(fake_cred)
        mock_log.info.assert_called_once_with("Initializing firestore connection...")

        del conn

    @patch("src.core.firestoreconnection.firebase_admin.initialize_app")
    @patch("src.core.firestoreconnection.Log")
    def test_initialize_firestore_raises_exception(self, mock_log_class, mock_initialize):
        """Method tests the initialization method failure route."""
        mock_log = MagicMock()
        mock_log_class.return_value = mock_log

        mock_initialize.side_effect = ValueError("Init failed")

        conn = FirestoreConnection("fake/path.json", "test_collection")

        with pytest.raises(ValueError):
            conn.initialize_firestore(MagicMock())

        del conn

    @patch("src.core.firestoreconnection.firestore.client")
    @patch("src.core.firestoreconnection.Log")
    def test_db_client_success(self, mock_log_class, mock_client):
        mock_log = MagicMock()
        mock_log_class.return_value = mock_log

        fake_db = MagicMock()
        mock_client.return_value = fake_db

        conn = FirestoreConnection("fake/path.json", "test_collection")

        result = conn.db_client()

        assert result is True
        mock_client.assert_called_once()
        mock_log.info.assert_called_once_with(
            "Firestore database client initialized successfully!"
        )

        del conn

    @patch("src.core.firestoreconnection.firestore.client")
    @patch("src.core.firestoreconnection.Log")
    def test_db_client_default_credentials_error(self, mock_log_class, mock_client):
        mock_log = MagicMock()
        mock_log_class.return_value = mock_log

        from google.auth.exceptions import DefaultCredentialsError
        mock_client.side_effect = DefaultCredentialsError("No credentials")

        conn = FirestoreConnection("fake/path.json", "test_collection")

        result = conn.db_client()

        assert result is False
        mock_log.error.assert_called_once_with(
            "Credentials returned DefaultCredentialsError!"
        )

        del conn

    @patch("src.core.firestoreconnection.Log")
    def test_save_collection_success(self, mock_log_class):
        mock_log = MagicMock()
        mock_log_class.return_value = mock_log

        conn = FirestoreConnection("fake/path.json", "test_collection")

        # Mock Firestore DB and collection chain
        mock_collection = MagicMock()
        mock_collection.get.return_value = ["doc1", "doc2"]

        mock_db = MagicMock()
        mock_db.collection.return_value = mock_collection

        conn.set_db(mock_db)

        result = conn.save_collection()

        assert result is True
        mock_db.collection.assert_called_once_with("test_collection")
        mock_collection.get.assert_called_once()
        assert conn.get_results() == ["doc1", "doc2"]

        del conn
