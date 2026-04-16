import unittest
import pandas as pd
from src.core.datareader import DataReader
from unittest.mock import MagicMock, patch

class TestDataReader(unittest.TestCase):
    """Class with tests of the DataReader."""

    def test_init(self):
        """Method tests the initialization of a class"""
        dr = DataReader()
        self.assertEqual(type(dr), DataReader)

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

    def test_normalize_firestore_like_object(self):
        dr = DataReader()

        mock_snapshot = MagicMock()
        mock_snapshot.to_dict.return_value = {"x": 10}

        result = dr._normalize([mock_snapshot])
        self.assertEqual(result, [{"x": 10}])
        mock_snapshot.to_dict.assert_called_once()

    def test_normalize_to_dict_not_callable(self):
        dr = DataReader()

        class BadObject:
            to_dict = {"not": "callable"}

        with self.assertRaises(TypeError):
            dr._normalize([BadObject()])

    def test_normalize_to_dict_returns_non_dict(self):
        dr = DataReader()

        mock_snapshot = MagicMock()
        mock_snapshot.to_dict.return_value = "not a dict"

        with self.assertRaises(TypeError):
            dr._normalize([mock_snapshot])

    def test_normalize_to_dict_raises_exception(self):
        dr = DataReader()

        mock_snapshot = MagicMock()
        mock_snapshot.to_dict.side_effect = Exception("Failure")

        with self.assertRaises(ValueError):
            dr._normalize([mock_snapshot])

    def test_normalize_unsupported_type(self):
        dr = DataReader()

        with self.assertRaises(TypeError):
            dr._normalize([1, 2, 3])

    def test_normalize_item_none(self):
        dr = DataReader()

        with self.assertRaises(TypeError):
            dr._normalize([None])

    def test_fetch_as_dicts_success(self):
        dr = DataReader()

        with patch.object(dr, "_normalize", return_value=[{"a": 1}]) as mock_norm:
            result = dr.fetch_as_dicts("dummy")

            self.assertEqual(result, [{"a": 1}])
            mock_norm.assert_called_once_with("dummy")

    def test_fetch_as_dicts_type_error(self):
        dr = DataReader()

        with patch.object(dr, "_normalize", side_effect=TypeError()):
            result = dr.fetch_as_dicts("dummy")
            self.assertIsNone(result)

    def test_fetch_as_dicts_value_error(self):
        dr = DataReader()

        with patch.object(dr, "_normalize", side_effect=ValueError()):
            result = dr.fetch_as_dicts("dummy")
            self.assertIsNone(result)

    def test_fetch_as_dicts_memory_error(self):
        dr = DataReader()

        with patch.object(dr, "_normalize", side_effect=MemoryError("Out of memory")):
            result = dr.fetch_as_dicts("dummy")
            self.assertIsNone(result)

    def test_fetch_as_dicts_logs_info(self):
        dr = DataReader()
        dr._DataReader__log = MagicMock()

        with patch.object(dr, "_normalize", return_value=[]):
            dr.fetch_as_dicts([])

            dr._DataReader__log.info.assert_called_once_with(
                "Saving data as dictionary..."
            )

    def test_fetch_as_dicts_logs_error_on_exception(self):
        dr = DataReader()
        dr._DataReader__log = MagicMock()

        with patch.object(dr, "_normalize", side_effect=TypeError("Bad type")):
            dr.fetch_as_dicts("dummy")

            self.assertTrue(dr._DataReader__log.error.called)

    def test_fetch_as_dataframe_success(self):
        dr = DataReader()

        with patch.object(dr, "_normalize", return_value=[{"a": 1}]):
            with patch("src.core.datareader.pd.DataFrame") as mock_df:
                mock_df.return_value = "DF_OBJECT"

                result = dr.fetch_as_dataframe("dummy")

                self.assertEqual(result, "DF_OBJECT")
                mock_df.assert_called_once_with([{"a": 1}])

    def test_fetch_as_dataframe_normalize_type_error(self):
        dr = DataReader()

        with patch.object(dr, "_normalize", side_effect=TypeError("Bad type")):
            result = dr.fetch_as_dataframe("dummy")
            self.assertIsNone(result)

    def test_fetch_as_dataframe_normalize_value_error(self):
        dr = DataReader()

        with patch.object(dr, "_normalize", side_effect=ValueError("None")):
            result = dr.fetch_as_dataframe("dummy")
            self.assertIsNone(result)

    def test_fetch_as_dataframe_normalize_memory_error(self):
        dr = DataReader()

        with patch.object(dr, "_normalize", side_effect=MemoryError("OOM")):
            result = dr.fetch_as_dataframe("dummy")
            self.assertIsNone(result)

    def test_fetch_as_dataframe_invalid_normalized_type(self):
        dr = DataReader()

        with patch.object(dr, "_normalize", return_value="not a list"):
            result = dr.fetch_as_dataframe("dummy")
            self.assertIsNone(result)

    def test_fetch_as_dataframe_dataframe_value_error(self):
        dr = DataReader()

        with patch.object(dr, "_normalize", return_value=[{"a": 1}]):
            with patch("src.core.datareader.pd.DataFrame", side_effect=ValueError("Bad DF")):
                result = dr.fetch_as_dataframe("dummy")
                self.assertIsNone(result)

    def test_fetch_as_dataframe_dataframe_type_error(self):
        dr = DataReader()

        with patch.object(dr, "_normalize", return_value=[{"a": 1}]):
            with patch("src.core.datareader.pd.DataFrame", side_effect=TypeError("Bad DF")):
                result = dr.fetch_as_dataframe("dummy")
                self.assertIsNone(result)

    def test_fetch_as_dataframe_dataframe_memory_error(self):
        dr = DataReader()

        with patch.object(dr, "_normalize", return_value=[{"a": 1}]):
            with patch("src.core.datareader.pd.DataFrame", side_effect=MemoryError("OOM")):
                result = dr.fetch_as_dataframe("dummy")
                self.assertIsNone(result)

    def test_fetch_as_dataframe_logs_info(self):
        dr = DataReader()
        dr._DataReader__log = MagicMock()

        with patch.object(dr, "_normalize", return_value=[]):
            with patch("src.core.datareader.pd.DataFrame", return_value=pd.DataFrame()):
                dr.fetch_as_dataframe([])

                dr._DataReader__log.info.assert_called_once_with(
                    "Saving data as dataframe..."
                )

    def test_fetch_as_dataframe_logs_error(self):
        dr = DataReader()
        dr._DataReader__log = MagicMock()

        with patch.object(dr, "_normalize", side_effect=TypeError("Bad type")):
            dr.fetch_as_dataframe("dummy")

            self.assertTrue(dr._DataReader__log.error.called)