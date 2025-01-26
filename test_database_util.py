"""
b5050d
1.25.2025

Tester of the function files
"""

import pytest
from database_util import *
import sqlite3


def get_fake_db_path(path, iter=0):
    a = path / f"test{iter}.db"
    return a

def create_fake_db(path):
    """
    Helper method, Creates a fake database
    """
    data = {
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35]
    }

    df = pd.DataFrame(data)

    conn = sqlite3.connect(path)

    df.to_sql('test', conn, if_exists='replace', index=False)

def create_empty_db(path):
    """
    Helper test method to create a blank db file
    """
    conn = sqlite3.connect(path)
    conn.close()

def test_init(tmp_path):
    """
    Test bringing up the class
    """
    fp = get_fake_db_path(tmp_path, 0)
    a = Database(fp)
    assert a.filepath

    with pytest.raises(ValueError):
        a = Database(tmp_path)

def test_load_database(tmp_path):
    """
    Test the load database function
    """
    fp = get_fake_db_path(tmp_path, 0)

    a = Database(fp)
    df = a.load_database()
    assert df.empty

    # what happens when the file exists but its empty?    
    create_empty_db(fp)
    df = a.load_database()
    assert df.empty

    #Alright what about when there is actually data in there?
    create_fake_db(fp)
    df = a.load_database()
    assert not df.empty
    print(df.to_string())


def test_add_row(tmp_path):
    fp = get_fake_db_path(tmp_path, 0)

    a = Database(fp)

    d = {"id": 4, "name": "Gerald", "age":348}
    # provide not a dict and error
    with pytest.raises(ValueError):
        a.add_row("hi there")
    
    # Add a row to a database that DNE
    a.add_row(d)

    df = a.load_database()
    assert not df.empty
    assert len(df) == 1

    # Add a row to a db that does exist but is empty

    # Add a row to a db that already exists, rows dont match

    # add a row to existing db but add an extra row

    # Add a row to a db that exists and perfectly match the rows
    fp = get_fake_db_path(tmp_path, 4)
    create_fake_db(fp)
    a = Database(fp)
    df = a.load_database()
    cols = df.columns.to_list()
    assert len(df) == 3
    a.add_row(d)
    df = a.load_database()
    new_cols = df.columns.to_list()
    assert len(df) == 4
    assert new_cols == cols





# def create_test_db(db_name):
#     """
#     Create a test database
#     """
#     conn = sqlite3.connect(db_name)
#     cursor = conn.cursor()

#     # Create a test table
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         email TEXT NOT NULL UNIQUE
#     )
#     """)

#     # Insert some test data
#     cursor.executemany("""
#     INSERT INTO users (name, email) VALUES (?, ?)
#     """, [
#         ("Alice", "alice@example.com"),
#         ("Bob", "bob@example.com"),
#         ("Charlie", "charlie@example.com")
#     ])

#     conn.commit()
#     conn.close()
#     # print(f"Database '{db_name}' created with test data.")


# def test_init_base(tmp_path):
#     with pytest.raises(ValueError):
#         a = Base(tmp_path)

#     a = Base(tmp_path / "test.db")
#     assert a.filepath

# def test_database_exist(tmp_path):
#     test_path = tmp_path / "test.db"
#     a = Base(test_path)

#     ans = a.database_exist()
#     assert not ans

#     # Now create a database
#     create_test_db(test_path)
#     ans = a.database_exist()
#     assert ans

# # def test_load_data(tmp_path):
# #     # Query db with nothing in it
# #     test_path = tmp_path / "test.db"

# #     a = Base(test_path)

# #     df = a.load_data()

# #     assert df.empty

# #     # Query a db with something in it


# # def test_add_row(tmp_path):
# #     # Add a row to a non existing database
# #     test_path = tmp_path / "test.db"

# #     a = Base(test_path)
# #     to_add = {"A": 1, "B": 2}
    
# #     a.add_row(to_add)
    



