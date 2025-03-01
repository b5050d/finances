"""
Written by b5050d

2.28.2025

Here is where my database classes will live
"""

import sqlite3
import pandas as pd
import os


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
        # self.sql_create_table = "SELECT * FROM expenses"

        self.sql_query_tables = "SELECT name FROM sqlite_master WHERE type='table';"
        self.sql_query_all = "SELECT * FROM {}"

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
    
    def query_all_in_table(self, tablename):
        """
        Query all the entries in a given table
        """
        with sqlite3.connect(self.database_path) as connection:
            df = pd.read_sql(self.sql_query_all.format(tablename), connection)
        return df


class ExpenseDatabase(FinancesDatabase):
    """
    Class for the Expense Database
    """

    def __init__(self, database_path):
        super().__init__(database_path)

        self.table_name = 'expenses'

        self.sql_create_table = f"""
CREATE TABLE IF NOT EXISTS {self.table_name} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    source TEXT NOT NULL,
    amount REAL NOT NULL
)
"""
        self.sql_add_row = "INSERT INTO expenses (category, source, amount) VALUES (?,?,?)"
        # self.sql_query_all = "SELECT * FROM expenses"

    def create_table(self):
        """
        Create a table
        """ 
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute(self.sql_create_table)

    def add_expense(self, category, source, amount):
        """
        Add an expense to the database
        """
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute(self.sql_add_row, (category, source, amount))

    def query_all_expenses(self):
        """
        Query all entries in the expense table
        and return as a dataframe
        """
        return self.query_all_in_table(self.table_name)


class IncomesDatabase(FinancesDatabase):
    """
    Class for the Incomes Database
    """
    def __init__(self, database_path):
        super().__init__(database_path)
        self.table_name = "incomes"
        self.sql_create_table = f"""
CREATE TABLE IF NOT EXISTS {self.table_name} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    source TEXT NOT NULL,
    amount REAL NOT NULL
)
"""
        self.sql_add_row = f"INSERT INTO {self.table_name} (category, source, amount) VALUES (?,?,?)"

    def create_table(self):
        """
        Create a table
        """ 
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute(self.sql_create_table)

    def add_income(self, category, source, amount):
        """
        Simply add an income row to the incomes db
        """
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute(self.sql_add_row, (category, source, amount))

    def query_all_incomes(self):
        """
        Query all entries in the income table
        and return as a dataframe
        """        
        return self.query_all_in_table(self.table_name)
