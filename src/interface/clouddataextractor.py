from src.core.firestoreconnection import FirestoreConnection
from src.exceptions.exceptions import CredentialsError, DBError


class CloudDataExtractor:
    """Class for extracting data from Firestore documents."""

    def __init__(self):
        """Constructor for CloudDataExtractor initializes firestore_connection with None."""
        self.__firestore_connection = None

    def set_firestore_connection(self, path):
        """Method for setting the firestore connection."""
        self.__firestore_connection = FirestoreConnection(path)

    def get_firestore_connection(self):
        """Method for getting the firestore connection."""
        return self.__firestore_connection

    def certificate_credentials(self, path):
        """Method for certificating the firestore credentials."""

        self.set_firestore_connection(path)
        success = self.__firestore_connection.certificate_credentials()
        try:
            if success:
                return self.__firestore_connection.get_credentials()
            else:
                raise CredentialsError()
        except CredentialsError as e:
                print(e.get_message())
                print("Error code: " + e.get_code())
                return None

    def initialize_app(self, credentials):
        """Method for initializing the application."""
        self.__firestore_connection.initialize_firestore(credentials)

    def db_client(self):
        """Method for getting the firestore database client."""
        success = self.__firestore_connection.db_client()
        try:
            if success:
                return self.__firestore_connection.get_db()
            else:
                raise DBError()
        except DBError as e:
            print(e.get_message())
            print("Error code: " + e.get_code())
            return None