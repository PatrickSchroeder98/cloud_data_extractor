import unittest
from src.exceptions.exceptions import CredentialsError, DBError


class TestExceptions(unittest.TestCase):
    """Class to test exceptions raised by application."""

    def test_CredentialsError_init(self):
        """Method to test CredentialsError Exception initialization."""
        e = CredentialsError()
        self.assertEqual(e.message, "Provided credentials returned error.")
        self.assertEqual(e.code, "CREDENTIALS_INVALID_001")
        del e

    def test_CredentialsError_get_message(self):
        """Method to test CredentialsError Exception get_message method."""
        e = CredentialsError()
        self.assertEqual(e.get_message(), "Provided credentials returned error.")
        del e

    def test_CredentialsError_get_code(self):
        """Method to test CredentialsError Exception get_code method."""
        e = CredentialsError()
        self.assertEqual(e.get_code(), "CREDENTIALS_INVALID_001")
        del e

    def test_DBError_init(self):
        """Method to test DBError Exception initialization."""
        e = DBError()
        self.assertEqual(e.message, "DB connection error.")
        self.assertEqual(e.code, "DB_CONNECTION_ERROR_002")
        del e

    def test_DBError_get_message(self):
        """Method to test DBError Exception get_message method."""
        e = DBError()
        self.assertEqual(e.get_message(), "DB connection error.")
        del e

    def test_DBError_get_code(self):
        """Method to test DBError Exception get_code method."""
        e = DBError()
        self.assertEqual(e.get_code(), "DB_CONNECTION_ERROR_002")
        del e