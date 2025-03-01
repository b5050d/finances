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
    fp = get_fake_db_path(tmp_path, 0)

    # Add a row to a db that already exists, rows dont match

    # add a row to existing db but add an extra column

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

