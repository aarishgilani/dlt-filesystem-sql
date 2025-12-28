"""
Pokemon Pipeline
=================
A simple DLT pipeline to fetch data from a public pokeapi.co REST API
and load it into the postgres data warehouse. 
"""

import dlt
from dlt.sources.helpers import requests

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


# Pipeline name is linked to the source and table for some reason
# Updated the name for API specific schema
pipeline = dlt.pipeline(
    pipeline_name="pokemon_api_pipeline",
    destination="postgres",
    dataset_name="pokemon_data",
)

# table name inferred from resource decorator
load_info = pipeline.run(fetch_pokemon_data)

print(load_info)