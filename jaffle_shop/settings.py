"""Settings for the jaffle shop data source"""

DATASET_NAME = "jaffle_shop_data"
DESTINATION = "postgres"
PIPELINE_NAME = "jaffle_shop_pipeline"
BUCKET_URL = "./filesystem/incoming"
FILE_GLOB = "*.csv"
FILE_PREFIX = "raw_"