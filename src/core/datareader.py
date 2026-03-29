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

        if not hasattr(results, "__iter__"):
            raise TypeError("Error! Results must be iterable.")

        normalized = []

        for item in results:
            if hasattr(item, "to_dict"):
                normalized.append(item.to_dict())
            elif isinstance(item, dict):
                normalized.append(item)
            else:
                self.__log.error("Unsupported result type!")
                raise TypeError(
                    f"Unsupported result type: {type(item)}"
                )

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
        