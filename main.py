from data import load_data, basic_query, office_query
import sqlite3 as sql


DATABASE_NAME = 'president_history'


def main():
    load_data('president_history')


if __name__ == "__main__":
    main()
