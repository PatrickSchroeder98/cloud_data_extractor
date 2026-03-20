import unittest
from src.exceptions.exceptions import CredentialsError, DBError, CollectionIsNone, ConnectionNotConfigured


class TestExceptions(unittest.TestCase):
    """Class to test exceptions raised by application."""

    def setUp(self):
        self.messages_and_codes = {
            "CredentialsError": {
                "message": "Provided credentials returned error.",
                "code": "CREDENTIALS_INVALID_001"
            },
            "DBError": {
                "message": "DB connection error.",
                "code": "DB_CONNECTION_ERROR_002"
            },
            "CollectionIsNone": {
                "message": "Collection is None, check the credentials and connection.",
                "code": "COLLECTION_NONE_ERROR_003"
            },
            "ConnectionNotConfigured": {
                "message": "Firestore connection not configured.",
                "code": "CONNECTION_NOT_CONFIGURED_004"
            }
        }

    def test_CredentialsError_init(self):
        """Method to test CredentialsError Exception initialization."""
        e = CredentialsError()
        self.assertEqual(e.message, self.messages_and_codes["CredentialsError"]["message"])
        self.assertEqual(e.code, self.messages_and_codes["CredentialsError"]["code"])
        del e

    def test_CredentialsError_get_message(self):
        """Method to test CredentialsError Exception get_message method."""
        e = CredentialsError()
        self.assertEqual(e.get_message(), self.messages_and_codes["CredentialsError"]["message"])
        del e

    def test_CredentialsError_get_code(self):
        """Method to test CredentialsError Exception get_code method."""
        e = CredentialsError()
        self.assertEqual(e.get_code(), self.messages_and_codes["CredentialsError"]["code"])
        del e

    def test_DBError_init(self):
        """Method to test DBError Exception initialization."""
        e = DBError()
        self.assertEqual(e.message, self.messages_and_codes["DBError"]["message"])
        self.assertEqual(e.code, self.messages_and_codes["DBError"]["code"])
        del e

    def test_DBError_get_message(self):
        """Method to test DBError Exception get_message method."""
        e = DBError()
        self.assertEqual(e.get_message(), self.messages_and_codes["DBError"]["message"])
        del e

    def test_DBError_get_code(self):
        """Method to test DBError Exception get_code method."""
        e = DBError()
        self.assertEqual(e.get_code(), self.messages_and_codes["DBError"]["code"])
        del e

    def test_CollectionIsNone_init(self):
        """Method to test CollectionIsNone Exception initialization."""
        e = CollectionIsNone()
        self.assertEqual(e.message, self.messages_and_codes["CollectionIsNone"]["message"])
        self.assertEqual(e.code, self.messages_and_codes["CollectionIsNone"]["code"])
        del e

    def test_CollectionIsNone_get_message(self):
        """Method to test CollectionIsNone Exception get_message method."""
        e = CollectionIsNone()
        self.assertEqual(e.get_message(), self.messages_and_codes["CollectionIsNone"]["message"])
        del e

    def test_CollectionIsNone_get_code(self):
        """Method to test CollectionIsNone Exception get_code method."""
        e = CollectionIsNone()
        self.assertEqual(e.get_code(), self.messages_and_codes["CollectionIsNone"]["code"])
        del e

    def test_ConnectionNotConfigured_init(self):
        """Method to test ConnectionNotConfigured Exception initialization."""
        e = ConnectionNotConfigured()
        self.assertEqual(e.message, self.messages_and_codes["ConnectionNotConfigured"]["message"])
        self.assertEqual(e.code, self.messages_and_codes["ConnectionNotConfigured"]["code"])
        del e

    def test_ConnectionNotConfigured_get_message(self):
        """Method to test ConnectionNotConfigured Exception get_message method."""
        e = ConnectionNotConfigured()
        self.assertEqual(e.get_message(), self.messages_and_codes["ConnectionNotConfigured"]["message"])
        del e

    def test_ConnectionNotConfigured_get_code(self):
        """Method to test ConnectionNotConfigured Exception get_code method."""
        e = ConnectionNotConfigured()
        self.assertEqual(e.get_code(), self.messages_and_codes["ConnectionNotConfigured"]["code"])
        del e
