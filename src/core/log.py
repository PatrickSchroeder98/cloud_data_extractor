import datetime
import os


class Log:
    """Class for logging functionality."""

    def __init__(self):
        """Constructor for Log class initializes the path."""
        self.__path = "log/log.txt"
        self.create_path()

    def set_path(self, path):
        """Method for setting the path of logging."""
        self.__path = path

    def get_path(self):
        """Method for getting the path of logging."""
        return self.__path

    def create_path(self):
        """Method for creating the path of logging."""
        if not os.path.exists(self.__path):
            os.makedirs(os.path.dirname(self.__path))

    def log(self, message):
        """Method for logging message."""
        with open(self.get_path(), "a") as file:
            now = self.get_now()
            file.write(now + " " + message + '\n')

    def get_now(self):
        """Method for getting the current time."""
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")