"""
Post Secondary Information System (PSIS) Pipeline Module
=========================================================
A DLT pipeline to load Postsecondary enrolments, by field of study, 
registration status, program type, credential type and gender data from
statistics canada open data portal into a Postgres data warehouse.
"""

import dlt
from dlt.common.typing import TDataItems
from dlt.sources.filesystem import filesystem, read_csv
from pendulum import datetime

@dlt.resource(table_name="psis_enrolments", write_disposition="replace", columns={"status": {"data_type": "text"}})
def parse_psis_enrolments() -> TDataItems:
    """
    Parses PSIS enrolment data from a CSV file.

    Yields:
        TDataItems: The parsed PSIS enrolment data dictionaries.
    """
    bucket_url = "./filesystem/incoming/"
    file_name = "37100011.csv"
    file = filesystem(bucket_url=bucket_url, file_glob=file_name)

    return (file | read_csv()).with_name("psis_enrolments")

pipeline: dlt.Pipeline = dlt.pipeline(
    pipeline_name="psis_data_pipeline",
    destination="postgres",
    dataset_name="psis_data",
)

print("Starting PSIS enrolments data pipeline...")
print("Source: Statistics Canada Open Data Portal - Post Secondary Information System (PSIS)")

info = pipeline.run(parse_psis_enrolments)

print(info)

print("PSIS enrolments data pipeline completed.")