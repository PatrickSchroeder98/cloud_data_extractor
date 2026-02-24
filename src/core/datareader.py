import pandas as pd
from src.core.log import Log


class DataReader:
    """Class responsible for reading extracting data and returning it in chosen format."""

    def __init__(self):
        self.__log = Log()

    def fetch_as_dicts(self, results):
        """Method returns results as a dictionary."""
        self.__log.info("Saving data as dictionary...")
        data = [doc.to_dict() for doc in results]
        return data

    def fetch_as_dataframe(self, results):
        """Method returns results as a dataframe."""
        self.__log.info("Saving data as dataframe...")
        data = [doc.to_dict() for doc in results]
        df = pd.DataFrame(data)
        return df

