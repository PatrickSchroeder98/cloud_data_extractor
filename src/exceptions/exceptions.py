class CredentialsError(Exception):
    """Exception raised for errors when credentials are invalid."""

    def __init__(
        self, message="Provided credentials returned error.", code="CREDENTIALS_INVALID_001"
    ):
        """Setting custom exception message."""
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)

    def get_message(self):
        """Gets the exception message."""
        return self.message

    def get_code(self):
        """Gets the exception code."""
        return self.code


class DBError(Exception):
    """Exception raised for errors with DB connection."""

    def __init__(
        self, message="DB connection error.", code="DB_CONNECTION_ERROR_002"
    ):
        """Setting custom exception message."""
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)

    def get_message(self):
        """Gets the exception message."""
        return self.message

    def get_code(self):
        """Gets the exception code."""
        return self.code

class CollectionIsNone(Exception):
    """Exception raised for errors with empty collection."""

    def __init__(
        self, message="Collection is None, check the credentials and connection.", code="COLLECTION_NONE_ERROR_003"
    ):
        """Setting custom exception message."""
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)

    def get_message(self):
        """Gets the exception message."""
        return self.message

    def get_code(self):
        """Gets the exception code."""
        return self.code

class ConnectionNotConfigured(Exception):
    """Exception raised for errors when connection is not configured."""

    def __init__(self, message="Firestore connection not configured.", code="CONNECTION_NOT_CONFIGURED_004"):
        """Setting custom exception message."""
        self.message = message
        self.code = code
        super().__init__(self.message, self.code)

    def get_message(self):
        """Gets the exception message."""
        return self.message

    def get_code(self):
        """Gets the exception code."""
        return self.code
