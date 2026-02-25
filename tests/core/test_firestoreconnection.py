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

    