import unittest
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
