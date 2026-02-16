import firebase_admin
from firebase_admin import credentials, firestore
from google.auth.exceptions import DefaultCredentialsError
from src.core.log import Log

class FirestoreConnection:
    """Class that handles firestore connection."""

    def __init__(self, path, collection_name):
        """Method for initializing firestore connection."""
        self.__path = path
        self.__credentials = None
        self.__db = None
        self.__collection_name = collection_name
        self.__results = None
        self.log = Log()

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

    def set_collection_name(self, collection_name):
        """Method for setting the collection name."""
        self.__collection_name = collection_name

    def get_collection_name(self):
        """Method for getting the collection name."""
        return self.__collection_name

    def set_results(self, results):
        """Method for setting the results of firestore connection."""
        self.__results = results

    def get_results(self):
        """Method for getting the results of firestore connection."""
        return self.__results

    def certificate_credentials(self):
        """Method for getting the firestore connection credentials."""
        try:
            self.__credentials = credentials.Certificate(self.get_path())
        except FileNotFoundError:
            self.log.error("File with credentials not found!")
            print("File with credentials not found!")
            self.__credentials = None
            return False
        except PermissionError:
            self.log.error("File with credentials returned PermissionError!")
            print("File with credentials returned PermissionError!")
            self.__credentials = None
            return False
        else:
            self.log.info("File with credentials loaded successfully!")
            return True

    def initialize_firestore(self, cred):
        """Method for initializing firestore connection."""
        self.log.info("Initializing firestore connection...")
        firebase_admin.initialize_app(cred)

    def db_client(self):
        """Method for getting the firestore database client."""
        try:
            self.set_db(firestore.client())
        except DefaultCredentialsError:
            self.log.error("Credentials returned DefaultCredentialsError!")
            print("Credentials returned DefaultCredentialsError!")
            return False
        else:
            self.log.info("Firestore database client initialized successfully!")
            return True

    def save_collection(self):
        """Method for getting the firestore collection."""
        try:
            self.set_results(self.get_db().collection(self.get_collection_name()).get())
        except AttributeError as e:
            self.log.error("Error! DB object is None.")
            print("Error! DB object is None.")
            return False
        else:
            return True
