from firebase_admin import credentials, firestore

class FirestoreConnection:
    """Class that handles firestore connection."""

    def __init__(self, path):
        """Method for initializing firestore connection."""
        self.path = path
        self.credentials = None

    def set_path(self, path):
        """Method for setting the path of firestore connection."""
        self.path = path

    def get_path(self):
        """Method for getting the path of firestore connection."""
        return self.path

    def set_credentials(self, cred):
        """Method for setting the credentials of firestore connection."""
        self.credentials = cred

    def get_credentials(self):
        """Method for getting the credentials of firestore connection."""
        return self.credentials

    def certificate_credentials(self):
        """Method for getting the firestore connection credentials."""
        try:
            self.credentials = credentials.Certificate(self.get_path())
        except FileNotFoundError:
            print("File with credentials not found!")
            self.credentials = None
            return False
        except PermissionError:
            print("File with credentials returned PermissionError!")
            self.credentials = None
            return False
        else:
            return True
