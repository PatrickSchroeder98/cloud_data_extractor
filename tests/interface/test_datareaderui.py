import unittest
from src.interface.datareaderui import DataReaderUI


class TestDataReaderUI(unittest.TestCase):
    """Tests for DataReaderUI."""

    def test_init(self):
        ui = DataReaderUI()
        self.assertEqual(type(ui), DataReaderUI)