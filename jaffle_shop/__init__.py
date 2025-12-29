"""
A source loading jaffle shop data from local filesystem
"""

import dlt
from typing import Sequence
from dlt.sources.filesystem import filesystem, read_csv
from .settings import BUCKET_URL, FILE_PREFIX
from dlt.sources import DltResource

@dlt.source(name="jaffle_shop")
def source() -> Sequence[DltResource]:
    """
    A dlt source for loading jaffle shop data from local filesystem. It reads CSV files from the specified directory.

    Args:
        bucket_url (str): The local directory path where the CSV files are stored. Defaults to "./filesystem".
        file_glob (str): The glob pattern to match CSV files. Defaults to "\*.csv".

    Returns:
        dlt.resource: A resource containing the loaded CSV data.
    """
    return (
        customers(),
        orders(),
        products(),
        stores(),
        supplies(),
    )


@dlt.resource(write_disposition="replace")
def customers() -> DltResource:
    """
    A dlt resource for loading customers data from customers.csv file in the filesystem.

    Returns:
        dlt.resource: A resource containing the customers data.
    """
    files = filesystem(bucket_url=BUCKET_URL, file_glob=f"{FILE_PREFIX}customers.csv")
    return (files | read_csv()).with_name("customers")

@dlt.resource(write_disposition="replace")
def orders() -> DltResource:
    """
    A dlt resource for loading orders data from orders.csv file in the filesystem.

    Returns:
        dlt.resource: A resource containing the orders data.
    """
    files = filesystem(bucket_url=BUCKET_URL, file_glob=f"{FILE_PREFIX}orders.csv")
    return (files | read_csv()).with_name("orders")

@dlt.resource(write_disposition="replace")
def products() -> DltResource:
    """
    A dlt resource for loading products data from products.csv file in the filesystem.

    Returns:
        dlt.resource: A resource containing the products data.
    """
    files = filesystem(bucket_url=BUCKET_URL, file_glob=f"{FILE_PREFIX}products.csv")
    return (files | read_csv()).with_name("products")

@dlt.resource(write_disposition="replace")
def stores() -> DltResource:
    """
    A dlt resource for loading stores data from stores.csv file in the filesystem.

    Returns:
        dlt.resource: A resource containing the stores data.
    """
    files = filesystem(bucket_url=BUCKET_URL, file_glob=f"{FILE_PREFIX}stores.csv")
    return (files | read_csv()).with_name("stores")

@dlt.resource(write_disposition="replace")
def supplies() -> DltResource:
    """
    A dlt resource for loading supplies data from supplies.csv file in the filesystem.
    
    Returns:
        dlt.resource: A resource containing the supplies data.
    """
    files = filesystem(bucket_url=BUCKET_URL, file_glob=f"{FILE_PREFIX}supplies.csv")
    return (files | read_csv()).with_name("supplies")


