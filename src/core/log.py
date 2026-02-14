import logging
import os
from pathlib import Path


class Log:
    """Logging wrapper around Python logging module."""

    def __init__(self, path: str = "log/logs.log"):
        self.__path = path
        self.__logger = None
        self._configure()

    def _configure(self):
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
        self.__logger.info(message)

    def warning(self, message: str):
        self.__logger.warning(message)

    def error(self, message: str):
        self.__logger.error(message)

    def debug(self, message: str):
        self.__logger.debug(message)