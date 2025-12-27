import dlt

# Sample data containing pokemon details
data = [
    {"id": "1", "name": "bulbasaur", "size": {"weight": 6.9, "height": 0.7}},
    {"id": "4", "name": "charmander", "size": {"weight": 8.5, "height": 0.6}},
    {"id": "25", "name": "pikachu", "size": {"weight": 6, "height": 0.4}},
    {"id": "39", "name": "jigglypuff", "size": {"weight": 5.5, "height": 0.5}},
]

# Set pipeline name, destination, and dataset name
pipeline = dlt.pipeline(
    pipeline_name="quick_start",
    destination="postgres",
    dataset_name="pokemon_data",
)

# specify table name else the process fails
# since the table name cannot be inferred from
# the data structure
load_info = pipeline.run(data, table_name="pokemon", write_disposition="merge", primary_key=["id"])

print(load_info)