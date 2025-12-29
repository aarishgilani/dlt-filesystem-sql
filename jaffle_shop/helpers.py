"""
Helper functions for the jaffle shop data pipeline.
"""

import hashlib

def pseudonymize_column(row, column: str) -> str:
    """
    Pseudonymizes a given column using a hashing function.

    Pseudonymization is a deterministic type of PII-obscuring.
    Its role is to allow identifying users by their hash,
    without revealing the underlying info.

    Args:
        row: The data row containing the column to be pseudonymized.
        column: The column to be pseudonymized.

    Returns:
        The pseudonymized column.
    """
    salt = "3rpq/JKV6Jw2zMb6kV9s4GO41ydET6hu"
    salted_column = row[column].strip() + salt
    salted_hash = hashlib.sha256()
    salted_hash.update(salted_column.encode())
    hash_hex = salted_hash.hexdigest() #string representation
    row[column] = hash_hex

    print(f"Pseudonymized {column}: {row[column]}")  # debug statement to trace computation values

    return row

def pseudonymize_name(row) -> str:
    """
    Pseudonymizes the 'name' column in the given row.

    Args:
        row: The data row containing the 'name' column.

    Returns:
        The pseudonymized 'name' column.
    """
    return pseudonymize_column(row, "name")
