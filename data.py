"""
Written by b5050d

2.28.2025
"""

import sqlite3
import pandas as pd
import os

TEST_DB = "data.db"

class FinancesDatabase:
    """
    Abstract Class used for Database mgmt
    """
    def __init__(self, database_path):
        self.database_path = database_path
        self._define_constants()
        self._define_sql_querys()

    def _define_constants(self):
        """
        Define constants needed for the class
        """
        self.INCOME_TABLE_NAME = "incomes"
        self.EXPENSE_TABLE_NAME = "expense"

    def _define_sql_querys(self):
        """
        Define the sqlite3 queries here that will
        be used
        """
        self.sql_create_table = ""

        self.sql_query_tables = "SELECT name FROM sqlite_master WHERE type='table';"

    def does_database_exist(self):
        """
        Check if the database exists
        """
        if os.path.exists(self.database_path):
            return True
        return False

    def query_existing_database_tables(self):
        """
        Get a list of the existing tables in the database
        """
        if self.does_database_exist():
            with sqlite3.connect(self.database_path) as connection:
                cursor = connection.cursor()
                cursor.execute(self.sql_query_tables)
                tables = cursor.fetchall()
                tables = [i[0] for i in tables]
            return tables
        return []


class ExpenseDatabase(FinancesDatabase):
    def __init__(self, database_path):
        super().__init__(database_path)

        self.sql_create_table = """
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
"""

    def create_table(self):
        pass
        # self.

    def add_expense(self):
        pass

    def query_all_expenses(self):
        """
        Query all entries in the expense table
        and return as a dataframe
        """
        pass

# class IncomesDatabase(FinancesDatabase):
#     def __init__(self, database_path):
#         super().__init__(database_path)


#     def add_income(self):
#         """
#         Query all entries in the income table
#         and return as a dataframe
#         """
        
#         pass










# sql_create_table = '''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER NOT NULL
# )
# '''
# sql = "INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25)
# table_query = "SELECT name FROM sqlite_master WHERE type='table';"
# # def get_database_connection

# def does_database_exist(database_path):


# def does_database_table_exist(database_path, table_name):
#     """
#     """
#     with 
#     # Query to fetch table names
# cursor.execute()

# # Fetch all results
# tables = cursor.fetchall()
    

# def query_existing_database_tables(database_path):



# # Create a cursor object
# cursor = conn.cursor()

# # Query to fetch table names
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# with sqlite3.connect(database_path) as conn:
#     cursor = conn.cursor()
#     cursor.execute(sql_create_table)
#     conn.commit()  # Ensure changes are saved
# # Fetch all results
# tables = cursor.fetchall()



# def create_table(database_path, table_name):
#     # Create a table
#     with sqlite3.connect(database_path) as connection:
#         cursor = connection.cursor()
#         cursor.execute(sql_create_table)

# def add_row(database_path):
#     """
#     Add a row to the database
#     """
#     conn = sqlite3.connect(database_path)

#     cursor = conn.cursor()

# def query_all():
#     """
#     Query all of the data 
#     """
#     pass

# if __name__ == "__main__":
#     create_table(TEST_DB)




