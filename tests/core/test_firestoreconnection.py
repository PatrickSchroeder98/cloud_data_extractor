import unittest
from src.core.firestoreconnection import FirestoreConnection


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
        firestore_connection = FirestoreConnection("example_path")
        path = "example_path_test"

        firestore_connection.set_path(path)
        self.assertEqual(firestore_connection.get_path(), path)

        del firestore_connection

    def test_get_path(self):
        """Method tests the getting the path of firestore connection."""
        firestore_connection = FirestoreConnection("example_path")
        path = "example_path"

        self.assertEqual(firestore_connection.get_path(), path)

        del firestore_connection
