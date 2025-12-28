"""
Dataframe Pipeline
==================
A simple DLT pipeline to load data from a pandas DataFrame into a Postgres data warehouse.
"""

import dlt
import pandas as pd

@dlt.resource(table_name="dataframe_table", write_disposition="append")
def fetch_dataframe_data():
    """
    Fetches CSV from cloud storage and yields it as a pandas dataframe.

    Yields:
        pd.DataFrame: A pandas DataFrame containing sample data.
    """
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
    data = pd.read_csv(url)
    yield data

pipeline = dlt.pipeline(
    pipeline_name="dataframe_pipeline",
    destination="postgres",
    dataset_name="dataframe_data",
)

info = pipeline.run(fetch_dataframe_data)
print(info)