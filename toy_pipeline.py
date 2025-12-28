import dlt
from dlt.sources.helpers import requests

# Sample data containing pokemon details

# TODO: Write a resource function to fetch data from a REST API
@dlt.resource(table_name="pokemon_api")
def fetch_pokemon_data():
    """
    Fetches pokemon data from the PokeAPI.
    Yields:
        List[Dict]: A list of pokemon data dictionaries.
    """
    url = "https://pokeapi.co/api/v2/pokemon"
    response = requests.get(url)
    print("Fetching data from PokeAPI...")
    print(response.json())
    yield response.json()["results"]

# Set pipeline name, destination, and dataset name
# Pipeline name is linked to the source and table for some reason
# Updated the name for API specific schema
pipeline = dlt.pipeline(
    pipeline_name="pokemon_api_pipeline",
    destination="postgres",
    dataset_name="pokemon_data",
)

# since the table name cannot be inferred from
# the data structure
load_info = pipeline.run(fetch_pokemon_data, table_name="pokemon_api")

print(load_info)