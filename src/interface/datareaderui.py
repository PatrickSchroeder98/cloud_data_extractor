from src.core.datareader import DataReader
from src.core.log import Log

class DataReaderUI:
    """Interface of DataReader."""

    def __init__(self):
        """Constructor creates instance of DataReader."""
        self.__log = Log()
        self.__dr = DataReader()

    def fetch_as_dicts(self, results):
        """Method returns results as a dictionary."""
        value = self.__dr.fetch_as_dicts(results)

        if value is None:
            #print("Results are None, check Error Logs for more information.")
            self.__log.error("Results are None, check Error Logs for more information.")
        return value

    def fetch_as_dataframe(self, results):
        """Method returns results as a dataframe."""
        value = self.__dr.fetch_as_dataframe(results)

        if value is None:
            #print("Results are None, check Error Logs for more information.")
            self.__log.error("Results are None, check Error Logs for more information.")
        return value
