"""
Pokemon Pipeline
=================
A simple DLT pipeline to fetch data from a public pokeapi.co REST API
and load it into the postgres data warehouse. 
"""

import dlt
from dlt.sources.helpers import requests
from dlt.common.typing import TDataItems

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

@dlt.transformer(data_from=fetch_pokemon_data, table_name="pokemon_api_details")
def pokemon_details(items: TDataItems) -> TDataItems:
    """
    Transformer to fetch detailed data for each pokemon.

    Args:
        items (TDataItems): The list of pokemon data dictionaries.

    Yields:
        TDataItems: The detailed pokemon data dictionaries.
    """
    for item in items:
        detail_url = item["url"]
        detail_response = requests.get(detail_url)
        yield detail_response.json()


# Pipeline name is linked to the source and table for some reason
# Updated the name for API specific schema
pipeline = dlt.pipeline(
    pipeline_name="pokemon_api_pipeline",
    destination="postgres",
    dataset_name="pokemon_data",
)

# table name inferred from resource decorator
load_info = pipeline.run(pokemon_details)

print(load_info)

print(pipeline.dataset().pokemon_api_details.df())