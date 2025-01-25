"""
b5050d
1.25.2025

Tester of the function files
"""

import pytest
from database_util import *
import sqlite3

def create_test_db(db_name):
    """
    Create a test database
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create a test table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """)

    # Insert some test data
    cursor.executemany("""
    INSERT INTO users (name, email) VALUES (?, ?)
    """, [
        ("Alice", "alice@example.com"),
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com")
    ])

    conn.commit()
    conn.close()
    # print(f"Database '{db_name}' created with test data.")


def test_init_base(tmp_path):
    with pytest.raises(ValueError):
        a = Base(tmp_path)

    a = Base(tmp_path / "test.db")
    assert a.filepath

def test_database_exist(tmp_path):
    test_path = tmp_path / "test.db"
    a = Base(test_path)

    ans = a.database_exist()
    assert not ans

    # Now create a database
    create_test_db(test_path)
    ans = a.database_exist()
    assert ans

# def test_load_data(tmp_path):
#     # Query db with nothing in it
#     test_path = tmp_path / "test.db"

#     a = Base(test_path)

#     df = a.load_data()

#     assert df.empty

#     # Query a db with something in it


# def test_add_row(tmp_path):
#     # Add a row to a non existing database
#     test_path = tmp_path / "test.db"

#     a = Base(test_path)
#     to_add = {"A": 1, "B": 2}
    
#     a.add_row(to_add)
    



