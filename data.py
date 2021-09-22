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
        pd.DataFrame: dataframe of queried data
    """
    conn = sql.connect(f'{database_name}.db')
    if isinstance(clause, int):
        queried_data = pd.read_sql(f'SELECT * FROM {table} WHERE start >= {clause} AND {clause} < end', conn)
    else:
        queried_data = pd.read_sql(f'SELECT * FROM {table} WHERE {column} = {clause}', conn)

    return queried_data


def office_query(database_name: str, office_year: int) -> str:
    """Queries for the office in a given year.

    Args:
        database_name (str): name of SQLite3 database
        office_year (int): year that the user wants to check

    Returns:
        pd.DataFrame: dataframes of queried data
    """
    conn = sql.connect(f'{database_name}.db')

    president_data = pd.read_sql(f'SELECT * from presidents where start >= {office_year} AND {office_year} < end', conn)
    vice_president_data = pd.read_sql(f'SELECT * from vice_presidents where start >= {office_year} AND {office_year} < end', conn)

    return president_data, vice_president_data


def Input_Parsing(input_str):
    query_list = input_str.split(" ")
    if len(query_list) == 3:
        if query_list[0] == "president" or query_list[0] == "vice-president" or query_list[0] == "office":
            return input_str  # Filler. Change later
        else:
            print("This input is not accepted. Your query should start with president, vice-president, or office.")
    else:
        print("This input is not accepted. Your query should exactly be three terms.")


def text_to_sql(input_str: str):

    t = input_str.split()
    query_param = {}

    if (t[0] == "president"):
        query_param["table"] = "presidents"
        query_param["clause"] = t[1]

    if (t[0] == "vice-president"):
        query_param["table"] = "vice-presidents"
        query_param["clause"] = t[1]

    if (t[0] == "office"):
        query_param["table"] = "Both"

        if (t[1] == "year"):
            query_param["clause"] = int(t[2])
            query_param["column"] = "All"

        if (t[1] == "number"):
            query_param["clause"] = t[2]
            query_param["column"] = "All"

    if (t[1] == "year" and t[0] != "office"):
        query_param["column"] = "year"
        query_param["clause"] = int(t[2])

    if (t[2] == "year"):
        query_param["column"] = "year"
        query_param["clause"] = t[1]

    if (t[1] == "name"):
        query_param["column"] = "All"
        query_param["clause"] = t[2]

    if (t[2] == "party"):
        query_param["column"] = "party"
        query_param["clause"] = t[1]

    if (t[2] == "vp"):
        query_param["table"] = "Both"
        query_param["column"] = "vp for clause"
        query_param["clause"] = t[1]

    if (t[2] == "p"):
        query_param["table"] = "Both"
        query_param["column"] = "p for clause"
        query_param["clause"] = t[1]

    if (t[1] == "number" and t[0] != "office"):
        query_param["column"] = "number"
        query_param["clause"] = t[2]

    if (t[2] == "number"):
        query_param["column"] = "number"
        query_param["clause"] = t[1]

    return query_param
