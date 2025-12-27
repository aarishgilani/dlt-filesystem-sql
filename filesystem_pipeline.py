"""
filesystem_pipeline.py
=========================
This module defines a data pipeline that loads all jaffle shop data from the filesystem
"""

import dlt
from jaffle_shop import source

def load_all_data() -> None:
    """Constructs a pipeline that will load all jaffle shop data from the filesystem."""

    pipeline = dlt.pipeline(
        pipeline_name="jaffle_shop_pipeline",
        destination='postgres',
        dataset_name="jaffle_shop_data", # defines the schema name in the destination
    )
    
    data = source()
    
    info = pipeline.run(data)
    print(info)

if __name__ == "__main__":
    load_all_data()