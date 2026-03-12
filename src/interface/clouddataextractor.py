from src.core.firestoreconnection import FirestoreConnection
from src.exceptions.exceptions import CredentialsError, DBError, CollectionIsNone, ConnectionNotConfigured
from src.core.log import Log


class CloudDataExtractor:
    """Class for extracting data from Firestore documents."""

    def __init__(self):
        """Constructor for CloudDataExtractor initializes firestore_connection with None."""
        self.__firestore_connection = None
        self.__log = Log()

    def set_firestore_connection(self, path, collection_name):
        """Method for setting the firestore connection."""
        self.__firestore_connection = FirestoreConnection(path, collection_name)

    def get_firestore_connection(self):
        """Method for getting the firestore connection."""
        return self.__firestore_connection

    def certificate_credentials(self):
        """Method for certificating the firestore credentials."""

        success = self.__firestore_connection.certificate_credentials()
        try:
            if success:
                return self.__firestore_connection.get_credentials()
            else:
                raise CredentialsError()
        except CredentialsError as e:
                self.__log.error(e.get_message())
                self.__log.error("Error code: " + e.get_code())
                return None

    def initialize_app(self, credentials):
        """Method for initializing the application."""
        try:
            if not self.__firestore_connection:
                raise ConnectionNotConfigured()
        except ConnectionNotConfigured as e:
            self.__log.error(e.get_message())
            self.__log.error("Error code: " + e.get_code())
            return None
        else:
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
            self.__log.error(e.get_message())
            self.__log.error("Error code: " + e.get_code())
            return None

    def db_get_collection(self):
        """Interface method for getting the firestore database collection."""
        return self.__firestore_connection.get_results()

    def extract_collection(self):
        """Interface method for saving the firestore collection."""
        success = self.__firestore_connection.save_collection()

        try:
            if success:
                return self.db_get_collection()
            else:
                raise CollectionIsNone()
        except CollectionIsNone as e:
            self.__log.error(e.get_message())
            self.__log.error("Error code: " + e.get_code())
            return None

    def extract_data(self, path, collection_name):
        """Method for extracting data from Firestore documents."""
        self.set_firestore_connection(path, collection_name)
        cred = self.certificate_credentials()
        self.initialize_app(cred)
        self.db_client()
        return self.extract_collection()