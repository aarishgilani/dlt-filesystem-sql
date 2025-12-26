import dlt
from dlt.sources.filesystem import filesystem, read_csv

files = filesystem(file_glob="*.csv")
reader = (files | read_csv()).with_name("raw_data")
pipeline = dlt.pipeline(pipeline_name="jaffle_shop_pipeline", dataset_name="jaffle_shop_data", destination="postgres")

info = pipeline.run(reader)
print(info);
