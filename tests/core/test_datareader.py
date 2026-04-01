import unittest
from src.core.datareader import DataReader


class TestDataReader(unittest.TestCase):
    """Class with tests of the DataReader."""

    def test_init(self):
        """Method tests the initialization of a class"""
        dr = DataReader()
        self.assertEqual(type(dr), DataReader)
        del dr

    def test_normalize_none(self):
        dr = DataReader()
        with self.assertRaises(ValueError):
            dr._normalize(None)

    def test_normalize_not_iterable(self):
        dr = DataReader()
        with self.assertRaises(TypeError):
            dr._normalize(123)

    def test_normalize_string_iterable_rejected(self):
        dr = DataReader()
        with self.assertRaises(TypeError):
            dr._normalize("string")

    def test_normalize_empty_iterable(self):
        dr = DataReader()
        result = dr._normalize([])
        self.assertEqual(result, [])

    def test_normalize_dict_items(self):
        dr = DataReader()
        data = [{"a": 1}, {"b": 2}]
        result = dr._normalize(data)

        self.assertEqual(result, data)
        self.assertIsNot(result[0], data[0])
        