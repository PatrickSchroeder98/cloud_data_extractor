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

        if not success:
            e = CredentialsError()
            self.__log.error(e.get_message())
            self.__log.error("Error code: " + e.get_code())
            return None

        return self.__firestore_connection.get_credentials()

    def initialize_app(self, credentials):
        """Method for initializing the application."""
        if not self.__firestore_connection:
            e = ConnectionNotConfigured()
            self.__log.error(e.get_message())
            self.__log.error("Error code: " + e.get_code())
            return None

        self.__firestore_connection.initialize_firestore(credentials)
        return None

    def db_client(self):
        """Method for getting the firestore database client."""

        if not self.__firestore_connection:
            e = ConnectionNotConfigured()
            self.__log.error(e.get_message())
            self.__log.error("Error code: " + e.get_code())
            return None

        success = self.__firestore_connection.db_client()

        if success:
            return self.__firestore_connection.get_db()

        e = DBError()
        self.__log.error(e.get_message())
        self.__log.error("Error code: " + e.get_code())
        return None

    def db_get_collection(self):
        """Interface method for getting the firestore database collection."""
        if not self.__firestore_connection:
            return None

        return self.__firestore_connection.get_results()

    def extract_collection(self):
        """Interface method for saving the firestore collection."""

        if not self.__firestore_connection:
            e = ConnectionNotConfigured()
            self.__log.error(e.get_message())
            self.__log.error("Error code: " + e.get_code())
            return None

        success = self.__firestore_connection.save_collection()

        if not success:
            e = CollectionIsNone()
            self.__log.error(e.get_message())
            self.__log.error("Error code: " + e.get_code())
            return None

        results = self.db_get_collection()

        if results is None:
            e = CollectionIsNone()
            self.__log.error(e.get_message())
            self.__log.error("Error code: " + e.get_code())
            return None

        return results

    def extract_data(self, path, collection_name):
        """Method for extracting data from Firestore documents."""

        self.set_firestore_connection(path, collection_name)

        cred = self.certificate_credentials()
        if not cred:
            return None

        self.initialize_app(cred)

        db = self.db_client()
        if not db:
            return None

        return self.extract_collection()
