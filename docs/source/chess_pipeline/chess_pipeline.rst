This module builds a data pipeline using chess game data fetched from an online source.

Chess.com Pipeline
==================

This pipeline demonstrates loading data from the Chess.com public API into a PostgreSQL database using `dlt`. It fetches player profiles, game archives, and online status.

Pipeline Components
-------------------

- **Data Source**: Chess.com public API.
- **ETL Tool**: `dlt` (data load tool) Python library.
- **Destination**: A PostgreSQL database instance.

Workflow
--------

The pipeline executes the following steps:

1.  **Initialization**: A `dlt` pipeline is initialized with the name `chess_pipeline`, a `postgres` destination, and the dataset name `chess_players_games_data`.
2.  **Data Loading**: The `chess` source is called with a list of player usernames and optional start and end months.
3.  **Resource Selection**: Specific resources are selected from the source, such as `players_games`, `players_profiles`, or `players_online_status`.
4.  **Table Creation**: `dlt` creates tables in the `chess_players_games_data` schema corresponding to the selected resources.
5.  **Data Insertion**: The data from the API is inserted into the corresponding tables.
6.  **Termination**: The pipeline run finishes, and load information is printed to the console.

Workflow Diagram
~~~~~~~~~~~~~~~~

.. mermaid::
   :name: chess_pipeline_workflow

   graph TD
      A[Start] --> B{Initialize dlt Pipeline};
      B --> C{Call chess source};

      subgraph "chess source"
         C --> R1[players_profiles]
         C --> R2[players_archives]
         C --> R3[players_games]
         C --> R4[players_online_status]
      end

      subgraph "Chess.com API"
         R1 --> E1[Player Profile Endpoint]
         R2 --> E2[Player Archives Endpoint]
         R3 --> E3[Player Games Endpoint]
         R4 --> E4[Player Online Status Endpoint]
      end

      E1 --> D{PostgreSQL Database};
      E2 --> D;
      E3 --> D;
      E4 --> D;
      D --> F[End];

Functions
---------

.. automodule:: chess_pipeline
   :members:

.. automodule:: chess
   :members: players_profiles, players_archives, players_games, players_online_status

.. admonition:: Laugh Time!
   :class: laughter

   Q: What is a chess player's favorite music? 
   
   A: Rook and Roll 😄