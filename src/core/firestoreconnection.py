import firebase_admin
from firebase_admin import credentials, firestore
from google.auth.exceptions import DefaultCredentialsError

class FirestoreConnection:
    """Class that handles firestore connection."""

    def __init__(self, path):
        """Method for initializing firestore connection."""
        self.__path = path
        self.__credentials = None
        self.__db = None

    def set_path(self, path):
        """Method for setting the path of firestore connection."""
        self.__path = path

    def get_path(self):
        """Method for getting the path of firestore connection."""
        return self.__path

    def set_credentials(self, cred):
        """Method for setting the credentials of firestore connection."""
        self.__credentials = cred

    def get_credentials(self):
        """Method for getting the credentials of firestore connection."""
        return self.__credentials

    def set_db(self, db):
        """Method for setting the database of firestore connection."""
        self.__db = db

    def get_db(self):
        """Method for getting the database of firestore connection."""
        return self.__db

    def certificate_credentials(self):
        """Method for getting the firestore connection credentials."""
        try:
            self.__credentials = credentials.Certificate(self.get_path())
        except FileNotFoundError:
            print("File with credentials not found!")
            self.__credentials = None
            return False
        except PermissionError:
            print("File with credentials returned PermissionError!")
            self.__credentials = None
            return False
        else:
            return True

    def initialize_firestore(self, cred):
        """Method for initializing firestore connection."""
        firebase_admin.initialize_app(cred)

    def db_client(self):
        """Method for getting the firestore database client."""
        try:
            self.set_db(firestore.client())
            return True
        except DefaultCredentialsError:
            print("Credentials returned DefaultCredentialsError!")
            return False