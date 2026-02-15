import logging
import os
from pathlib import Path


class Log:
    """Logging wrapper around Python logging module."""

    def __init__(self, path: str = "log/logs.log"):
        """Constructor sets required attributes."""
        self.__path = path
        self.__logger = None
        self._configure()

    def _configure(self):
        """Method configures logging module."""
        log_path = Path(self.__path)

        # Create directory ONLY
        log_path.parent.mkdir(parents=True, exist_ok=True)

        self.__logger = logging.getLogger("Cloud Data Extractor")
        self.__logger.setLevel(logging.INFO)

        if not self.__logger.handlers:
            handler = logging.FileHandler(
                self.__path,
                encoding="utf-8"
            )

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )

            handler.setFormatter(formatter)
            self.__logger.addHandler(handler)

    def info(self, message: str):
        """Method logs information message."""
        self.__logger.info(message)

    def warning(self, message: str):
        """Method logs warning message."""
        self.__logger.warning(message)

    def error(self, message: str):
        """Method logs error message."""
        self.__logger.error(message)

    def debug(self, message: str):
        """Method logs debug message."""
        self.__logger.debug(message)