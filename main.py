from data import load_data, basic_query, office_query, input_parsing, text_to_sql
import sqlite3 as sql
from tabulate import tabulate
import pandas as pd


DATABASE_NAME = 'president_history'


def main():
    print('Attempting loading data...')
    try:
        load_data('president_history')
    except ValueError:
        print('Data already loaded!')
        pass

    done = False
    while not done:
        query = input('Please enter a query: ')
        if input_parsing(query) is not None:
            query_structure = text_to_sql(query)
            print(query_structure)

            if query_structure['table'] != 'Both' or 'p for clause' in query_structure['column']:
                data = [basic_query(DATABASE_NAME, query_structure['table'], query_structure['column'], query_structure['clause'])]
            else:
                data = office_query(DATABASE_NAME, query_structure['clause'])

            for d in data:
                if isinstance(d, pd.DataFrame):
                    print(tabulate(d, headers='keys', tablefmt='psql', showindex=False))
                else:
                    print(d)


            again = input('Would you like to query again? (Y/n) ')
            if again.lower() != 'y':
                done = True


if __name__ == "__main__":
    main()
