import json
import pandas as pd
from src.core.log import Log


class DataReader:
    """Class responsible for reading the extracted data and returning it in chosen format."""

    def __init__(self):
        """Class constructor initializes Log."""
        self.__log = Log()

    def _normalize(self, results):
        """Converts Firestore DocumentSnapshots or dictionaries into a list of dictionaries."""
        if results is None:
            self.__log.error("Error! Results is None.")
            raise ValueError("Results cannot be None.")

        # Prevent strings and bytes from being treated as valid iterables
        if isinstance(results, (str, bytes)):
            raise TypeError("Results must be a non-string iterable.")

        try:
            iterator = iter(results)
        except TypeError:
            raise TypeError("Results must be iterable.")

        normalized = []

        for item in iterator:
            if item is None:
                raise TypeError("Items in results cannot be None.")

            # Firestore-like object
            if hasattr(item, "to_dict"):
                method = getattr(item, "to_dict")

                if not callable(method):
                    raise TypeError("to_dict attribute must be callable.")

                try:
                    value = method()
                except Exception as e:
                    raise ValueError("to_dict() raised an exception.") from e

                if not isinstance(value, dict):
                    raise TypeError("to_dict() must return a dictionary.")

                normalized.append(value.copy())

            elif isinstance(item, dict):
                normalized.append(item.copy())

            else:
                self.__log.error("Unsupported result type!")
                raise TypeError(f"Unsupported result type: {type(item)}")

        return normalized

    def fetch_as_dicts(self, results):
        """Method to fetch data as dictionaries."""
        self.__log.info("Saving data as dictionary...")
        try:
            data = self._normalize(results)
        except TypeError:
            self.__log.error("TypeError: Results must be iterable.")
            return None
        except ValueError:
            self.__log.error("ValueError: Results cannot be None.")
            return None
        except MemoryError as e:
            self.__log.error(f"DataFrame creation failed with MemoryError: {e}")
            return None
        else:
            return data

    def fetch_as_dataframe(self, results):
        """Method to fetch data as Pandas dataframe."""
        self.__log.info("Saving data as dataframe...")

        try:
            data = self._normalize(results)
        except TypeError:
            self.__log.error("TypeError: Results must be iterable.")
            return None
        except ValueError:
            self.__log.error("ValueError: Results cannot be None.")
            return None
        except MemoryError as e:
            self.__log.error(f"DataFrame creation failed with MemoryError: {e}")
            return None

        try:
            return pd.DataFrame(data)
        except ValueError as e:
            self.__log.error(f"DataFrame creation failed with ValueError: {e}")
            return None
        except TypeError as e:
            self.__log.error(f"DataFrame creation failed with TypeError: {e}")
            return None
        