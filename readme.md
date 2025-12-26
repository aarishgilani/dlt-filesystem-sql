# DLT (Data Loading Tool)

The goal of this project is to build data pipeline to combine raw data from different sources. This tool helps facilitate transformation of data using DBT inside the warehouse to provide self-service data outlet for analysts and internal stakeholders. 

---

## Toy Pipeline Demo

This pipeline demonstrates a simple data loading process using the `dlt`. It loads a predefined list of Pokémon data into a PostgreSQL database.

### Pipeline Components

- **Data Source**: A static list of Pokémon data defined within the Python script.
- **ETL Tool**: `dlt` (data load tool) Python library used to create and run the pipeline.
- **Destination**: A PostgreSQL database instance.

### Workflow

The pipeline executes the following steps:

1.  **Initialization**: `dlt` pipeline is initialized with a specified pipeline name, destination, and dataset name.
2.  **Data Loading**: Sample Pokémon data is loaded into a PostgreSQL table named `pokemon` within the `pokemon_data` dataset (schema).
3.  **Termination**: The pipeline run finishes, and information about the load is printed to the console.

#### Workflow Diagram

```mermaid
graph TD
    A[Start] --> B{Initialize dlt Pipeline};
    B --> C[Load Pokémon Data];
    C --> D{Write to PostgreSQL};
    D --> E[End];
```

#### Data Schema

The data being processed has the following structure:

- `id`: (string) The Pokémon's ID.
- `name`: (string) The Pokémon's name.
- `size`: (object) An object containing the Pokémon's size information.
    - `weight`: (float) The Pokémon's weight.
    - `height`: (float) The Pokémon's height.

The data is loaded into a table named `pokemon`. `dlt` will creates following columns:

- `id` (text)
- `name` (text)
- `size__weight` (float)
- `size__height` (float)
- `_dlt_load_id` (text)
- `_dlt_id` (text)

The `size` object is flattened into separate columns `size__weight` and `size__height` by `dlt`. The `_dlt_load_id` and `_dlt_id` columns are added by `dlt` for internal tracking.

