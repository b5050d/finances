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

def all_list_items_match(a_list, b_list):
    """
    Check if all the items are matching between 2 lists
    Order agnostic
    """
    result = True
    for a in a_list:
        if a not in b_list:
            result = False
    for b in b_list:
        if b not in a_list:
            result = False
    return result

class Database:
    """
    Database class to abstract sqlite3 ops into easy stuff
    """
    def __init__(self, filepath):
        """
        Bring up the class
        """
        self.TABLE = 'test' # TODO find a way to not fix the table name
        filepath = str(filepath)
        if ".db" not in filepath:
            raise ValueError("Need .db file")
        self.filepath = filepath

    def load_database(self):
        """
        Load the database into a dataframe
        """
        # if the database does not exist
        if not os.path.exists(self.filepath):
            return pd.DataFrame()
        
        # Try to open it
        try:
            conn = sqlite3.connect(self.filepath)
            query= "SELECT * from {}".format(self.TABLE)
            df = pd.read_sql(query, conn)
        except pd.errors.DatabaseError:
            df = pd.DataFrame()
        finally:
            conn.close()
        return df
    
    def _write_df_to_db(self, df, overwrite = False):
        """
        Write the dataframe to the database
        """
        if overwrite:
            conn = sqlite3.connect(self.filepath)
            df.to_sql(self.TABLE, conn, if_exists='replace', index = False)
            conn.close()
        else:
            conn = sqlite3.connect(self.filepath)
            df.to_sql(self.TABLE, conn, if_exists='append', index = False)
            conn.close()
    
    def add_row(self, row_data):
        """
        Add a row to the database

        TODO - if this gets slow, maybe look into appending
        rows and not just overwriting the whole db
        """
        if type(row_data) is not dict: raise ValueError("provide dict")
        
        df = self.load_database()

        if df.empty:
            df = pd.DataFrame([row_data])
            self._write_df_to_db(df, overwrite =True)

        else:
            existing_cols = df.columns.to_list()
            new_cols = list(row_data.keys())

            if all_list_items_match(existing_cols, new_cols):
                new_df = pd.DataFrame([row_data])
                df = pd.concat([df, new_df], ignore_index=True)
                self._write_df_to_db(df, overwrite=True)
            else:
                pass
                # soemthigs fucky

            









# @contextmanager
# def db_connection(db_path):
#     conn = sqlite3.connect(db_path)
#     try:
#         yield conn
#     finally:
#         conn.close()
#         for i in range(1000): print("Connection closed.")

# class Base():
#     """
    
#     """
#     def __init__(self, filepath):
#         """
#         Bring up the class
#         """
#         filepath = str(filepath)
#         if ".db" not in str(filepath):
#             raise ValueError("Filepath is not correct")
#         self.filepath = filepath
#         self.table_name = "Table"

#     def database_exist(self):
#         if os.path.exists(self.filepath):
#             return True
#         else:
#             return False

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

    









