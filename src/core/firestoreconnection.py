class FirestoreConnection:
    """Class that handles firestore connection."""

    def __init__(self):
        """Method for initializing firestore connection."""
        self.path = None

    def set_path(self, path):
        """Method for setting the path of firestore connection."""
        self.path = path

    def get_path(self):
        """Method for getting the path of firestore connection."""
        return self.path
    