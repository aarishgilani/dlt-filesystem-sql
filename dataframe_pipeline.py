"""
Dataframe Pipeline
==================
A simple DLT pipeline to load data from a pandas DataFrame into a Postgres data warehouse.
"""

import dlt
import pandas as pd

# TODO : Create a resource function that yields data from a pandas DataFrame 
@dlt.resource(table_name="dataframe_table")
