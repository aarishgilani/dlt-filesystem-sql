This module builds a data pipeline using .csv files stored in the local filesystem.

.. note::
   The resources are replaced on each pipeline run to ensure 
   latest data is loaded from the filesystem. Since the data 
   is considerably small, full refresh is used instead of 
   incremental loading.

Jaffle Shop Pipeline
====================

This pipeline demonstrates loading data from a local filesystem into a PostgreSQL database using `dlt`. It reads multiple CSV files representing Jaffle Shop data and loads them into separate tables.

Pipeline Components
-------------------

- **Data Source**: CSV files (``customers.csv``, ``orders.csv``, ``products.csv``, ``stores.csv``, ``supplies.csv``) located in the ``filesystem/incoming`` directory.
- **ETL Tool**: ``dlt`` (data load tool) Python library.
- **Destination**: A PostgreSQL database instance.

Workflow
--------

The pipeline executes the following steps:

1.  **Initialization**: A ``dlt`` pipeline is initialized with the name ``jaffle_shop_pipeline``, a ``postgres`` destination, and the dataset name ``jaffle_shop_data``.
2.  **Data Loading**: The ``jaffle_shop`` source reads the various CSV files from the filesystem.
3.  **Table Creation**: ``dlt`` creates tables in the ``jaffle_shop_data`` schema corresponding to the CSV files (``customers``, ``orders``, ``products``, ``stores``, ``supplies``).
4.  **Data Insertion**: The data from the CSV files is inserted into the corresponding tables.
5.  **Termination**: The pipeline run finishes, and load information is printed to the console.

Workflow Diagram
~~~~~~~~~~~~~~~~

.. mermaid::
   :name: filesystem_pipeline_workflow

   graph TD
      A[Start] --> B{Initialize dlt Pipeline};
      B --> C{Call jaffle_shop source};

      subgraph "jaffle_shop source"
         C --> R1[customers resource]
         C --> R2[orders resource]
         C --> R3[products resource]
         C --> R4[stores resource]
         C --> R5[supplies resource]
      end

      subgraph "Filesystem (CSV files)"
         R1 --> F1[customers.csv]
         R2 --> F2[orders.csv]
         R3 --> F3[products.csv]
         R4 --> F4[stores.csv]
         R5 --> F5[supplies.csv]
      end

      subgraph "PostgreSQL (jaffle_shop_data schema)"
         F1 --> T1[customers table]
         F2 --> T2[orders table]
         F3 --> T3[products table]
         F4 --> T4[stores table]
         F5 --> T5[supplies table]
      end

      T1 --> Z[End]
      T2 --> Z
      T3 --> Z
      T4 --> Z
      T5 --> Z
      
Data Schema
-----------

The pipeline creates the following tables in the ``jaffle_shop_data`` schema in the PostgreSQL database:

- ``customers``
- ``orders``
- ``products``
- ``stores``
- ``supplies``

The columns in each table are inferred by ``dlt`` from the headers in the respective CSV files. ``dlt`` also adds its own metadata columns (``_dlt_load_id``, ``_dlt_id``) for internal tracking.

.. seealso:: 
   https://github.com/aarishgilani/jaffle-shop-dbt DBT project that 
   utilizes the data loaded by this pipeline for further transformations and analysis.
   Creating a self-service analytics stack using DLT, DBT, and PowerBI. T (Transform) 
   part of the ELT (Extract, Load, Transform) process is handled by DBT in this case.

Technical Documentation
-----------------------

Entry point for the filesystem pipeline:

.. automodule:: filesystem_pipeline
   :members:

The ``filesystem_pipeline`` data source has following resources:

.. autofunction:: jaffle_shop.source
.. autofunction:: jaffle_shop.customers
.. autofunction:: jaffle_shop.orders
.. autofunction:: jaffle_shop.products
.. autofunction:: jaffle_shop.stores
.. autofunction:: jaffle_shop.supplies 

.. admonition:: Laugh Time!
   :class: laughter

   A SQL query walks into a bar, walks up to two tables, and asks, “Can I join you?”  😂

  