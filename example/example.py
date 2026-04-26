"""
This file shows the example usage of the library
Data are loaded from GCP into a data frame with the usage of
extract_data and fetch_as_dataframe methods.
"""

from src.interface.clouddataextractor import CloudDataExtractor
from src.interface.datareaderui import DataReaderUI


cde = CloudDataExtractor()
dr = DataReaderUI()

results = cde.extract_data("key.json", "orders")
data = dr.fetch_as_dataframe(results)
print(data)
