import unittest
import logging
from unittest.mock import patch, MagicMock
from pathlib import Path
from src.core.log import Log


class TestFirestoreConnection(unittest.TestCase):
    """Class with tests of the Log wrapper."""

    @patch("src.core.log.Path.mkdir")
    @patch("src.core.log.logging.FileHandler")
    @patch("src.core.log.logging.getLogger")
    def test_log_init_creates_logger(self, mock_get_logger, mock_filehandler, mock_mkdir):

        fake_logger = MagicMock()
        fake_logger.handlers = []
        mock_get_logger.return_value = fake_logger

        log = Log("logs/test.log")

        mock_mkdir.assert_called_once_with(parents=True, exist_ok=True)
        mock_get_logger.assert_called_once_with("Cloud Data Extractor")
        fake_logger.setLevel.assert_called_once_with(logging.INFO)
        mock_filehandler.assert_called_once_with("logs/test.log", encoding="utf-8")
        fake_logger.addHandler.assert_called_once()
