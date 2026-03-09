import unittest
from src.core.datareader import DataReader

class TestDataReader(unittest.TestCase):
    """Class with tests of the DataReader."""

    def test_init(self):
        """Method tests the initialization of a class"""
        dr = DataReader()
        self.assertEqual(type(dr), DataReader)
        del dr
