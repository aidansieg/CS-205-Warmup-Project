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
    table = table.replace('-', '_')

    if isinstance(clause, int):
        queried_data = pd.read_sql(f'SELECT * FROM {table} WHERE {clause} BETWEEN start AND end', conn)
    elif column == 'All':
        clause = clause.replace('-', ' ').title()
        queried_data = pd.read_sql(f'SELECT * FROM {table} WHERE name == "{clause}"', conn)
    elif column == 'party':
        clause = clause.replace('-', ' ').title()
        queried_data = pd.read_sql(f'SELECT * FROM {table} WHERE name == "{clause}"', conn)['party'].values[0]
    elif column == 'number':
        clause = clause.replace('-', ' ').title()
        queried_data = pd.read_sql(f'SELECT * FROM {table} WHERE number == "{clause}"', conn)
    elif column == 'year':
        clause = clause.replace('-', ' ').title()
        queried_data = pd.read_sql(f'SELECT * FROM {table} WHERE name == "{clause}"', conn)['start'].values
    elif column == 'vp for clause':
        clause = clause.replace('-', ' ').title()
        president_df = pd.read_sql(f'SELECT * FROM presidents WHERE name == "{clause}"', conn)
        start = president_df['start'].values[0]
        end = president_df['end'].values[0]
        vp_df = pd.read_sql(f'SELECT * from vice_presidents where start == {start} AND end == {end}', conn)
        queried_data = vp_df['name'].values[0]
    elif column == 'p for clause':
        clause = clause.replace('-', ' ').title()
        vice_president_df = pd.read_sql(f'SELECT * FROM vice_presidents WHERE name == "{clause}"', conn)
        start = vice_president_df['start'].values[0]
        end = vice_president_df['end'].values[0]
        p_df = pd.read_sql(f'SELECT * from presidents where start == {start} AND end == {end}', conn)
        queried_data = p_df['name'].values[0]
    else:
        queried_data = pd.read_sql(f'SELECT * FROM {table} WHERE {column} == {clause}', conn)

    if isinstance(queried_data, pd.DataFrame):
        try:
            cols_to_drop = ['index', 'Unnamed: 0']
            for col in cols_to_drop:
                queried_data.drop(columns=[col], inplace=True)
        except:
            pass

    return queried_data


def office_query(database_name: str, office_year_or_number: int) -> str:
    """Queries for the office in a given year.

    Args:
        database_name (str): name of SQLite3 database
        office_year (int): year that the user wants to check

    Returns:
        pd.DataFrame: dataframes of queried data
    """
    conn = sql.connect(f'{database_name}.db')

    if len(str(office_year_or_number)) >= 4:
        president_data = pd.read_sql(f'SELECT * from presidents where {office_year_or_number} BETWEEN start AND end', conn)
        vice_president_data = pd.read_sql(f'SELECT * from vice_presidents where {office_year_or_number} BETWEEN start AND end', conn)
    else:
        president_data = pd.read_sql(f'SELECT * from presidents where number == {office_year_or_number}', conn)
        vice_president_data = pd.read_sql(f'SELECT * from vice_presidents where number == {office_year_or_number}', conn)

    data = [president_data, vice_president_data]
    for df in data:
        try:
            cols_to_drop = ['index', 'Unnamed: 0']
            for col in cols_to_drop:
                data.drop(columns=[col], inplace=True)
        except:
            pass

    return data


def input_parsing(input_str: str):
    """Validate that what the suer entered is something the program can use.

    Args:
        input_str (str): user query

    Returns:
        Union[str, None]: returns the user input if valid, otherwise None.
    """
    query_list = input_str.split(" ")
    if len(query_list) == 3:
        if query_list[0] == "president" or query_list[0] == "vice-president" or query_list[0] == "office":
            return input_str  # Filler. Change later
        else:
            print("This input is not accepted. Your query should start with president, vice-president, or office.")
    else:
        print("This input is not accepted. Your query should exactly be three terms.")

    return None


def text_to_sql(input_str: str) -> dict:
    """Turn a validated input string into a dict that can be mapped to SQL.

    Args:
        input_str (str): validated user input

    Returns:
        dict: dict of key value pairs to be used in SQL query
    """
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
