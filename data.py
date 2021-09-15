import sqlite3 as sql
import pandas as pd
from typing import Union


def load_data(database_name: str) -> None:
    """Load the president and vice president data into SQLite3 database.

    Args:
        database_name (str): name of the SQLite3 database
    """
    pres_df = pd.read_csv('us_presidents.csv')
    vice_df = pd.read_csv('us_vicepresidents.csv')
    assert len(pres_df) > 0
    assert len(vice_df) > 0
    print(f'Read aded {len(pres_df)} rows of president data and {len(vice_df)} rows of vice president data.')
    conn = sql.connect(f'{database_name}.db')
    pres_df.to_sql('presidents', conn)
    vice_df.to_sql('vice_presidents', conn)
    print('Successfully loaded data into SQLite database.')


def basic_query(database_name: str, table: str, column: str, clause: Union[str, int]) -> str:
    """A basic query for our database that is used on a single table

    Args:
        database_name (str): the name of the SQLite3 database
        table (str): table to query from
        column (str): column to check
        clause (Union[str, int]): column value we are searching for

    Returns:
        str: string to be shown to user
    """
    conn = sql.connect(f'{database_name}.db')
    if isinstance(clause, int):
        queried_data = pd.read_sql(f'SELECT * FROM {table} WHERE start >= {clause} AND {clause} < end', conn)
    else:
        queried_data = pd.read_sql(f'SELECT * FROM {table} WHERE {column} = {clause}', conn)

    return queried_data


def office_query(database_name: str, office_year: int) -> str:
    pass
