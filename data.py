import sqlite3 as sql
import pandas as pd


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
