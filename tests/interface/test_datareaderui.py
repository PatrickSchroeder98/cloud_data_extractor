import unittest
from unittest.mock import MagicMock
from src.interface.datareaderui import DataReaderUI


class TestDataReaderUI(unittest.TestCase):
    """Tests for DataReaderUI."""

    def test_init(self):
        ui = DataReaderUI()
        self.assertEqual(type(ui), DataReaderUI)

    def test_fetch_as_dicts_success(self):
        ui = DataReaderUI()
        ui._DataReaderUI__dr = MagicMock()
        ui._DataReaderUI__dr.fetch_as_dicts.return_value = [{"a": 1}]

        result = ui.fetch_as_dicts("input")

        self.assertEqual(result, [{"a": 1}])
        ui._DataReaderUI__dr.fetch_as_dicts.assert_called_once_with("input")
