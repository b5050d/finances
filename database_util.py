"""
b5050d
1.25.2025

Holder of functions (for now)
"""
import os
import sqlite3
import pandas as pd
from contextlib import contextmanager

"""
What methods do I need?

Load the table from the database, probably into a dataframe

"""

@contextmanager
def db_connection(db_path):
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()
        for i in range(1000): print("Connection closed.")


class Base():
    """
    
    """
    def __init__(self, filepath):
        """
        Bring up the class
        """
        filepath = str(filepath)
        if ".db" not in str(filepath):
            raise ValueError("Filepath is not correct")
        self.filepath = filepath
        self.table_name = "Table"

    def database_exist(self):
        if os.path.exists(self.filepath):
            return True
        else:
            return False

    # def get_tables_present(self):
    #     """
    #     Get Tables List of tables present
    #     in the database
    #     """
    #     if not self.database_exist():
    #         return pd.Dataframe()
        
    #     with db_connection(self.filepath) as conn:
    #         cursor = conn.cursor()
    #         cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    #         tables = cursor.fetchall()
    #         table_list = [table[0] for table in tables]
    #         conn.close()
    #         return table_list

    # def does_table_exist(self):
    #     """
    #     Does the table exist?
    #     """
    #     tables_list = self.get_tables_present()
    #     if self.table_name in tables_list:
    #         return True
    #     else:
    #         return False

    # def make_connection(self):
    #     conn = sqlite3.connect(self.filepath)
    #     return conn

    # def load_data(self):
    #     """
    #     Load the data in the database
    #     """

    #     conn = self.make_connection()
    #     query = f"SELECT * FROM {self.table_name}"
    #     df = pd.read_sql_query(query, conn)
    #     return df

    # def add_row(self, data):
    #     pass

    









