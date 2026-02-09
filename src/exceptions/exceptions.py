class CredentialsError(Exception):
    """Exception raised for errors when credentials invalid."""

    def __init__(
        self, message="Provided credentials returned error.", code="CR_INVALID_001"
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