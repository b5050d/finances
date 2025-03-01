"""
Written by b5050d

2.28.2025
"""

import pytest
import os

from data import *
import sqlite3

@pytest.fixture()
def provision_expense_database(tmp_path):
    fp = tmp_path / "test.db"
    return ExpenseDatabase(fp)

def test_expense_init(provision_expense_database):
    expenses = provision_expense_database
    assert expenses.database_path

def test_does_database_exist(provision_expense_database):
    expenses = provision_expense_database
    assert not expenses.does_database_exist()
    with open(expenses.database_path, "wb") as f:
        f.write(b"b")
    assert expenses.does_database_exist()

def test_query_existing_database_tables(provision_expense_database):
    expenses = provision_expense_database
    ans = expenses.query_existing_database_tables()
    assert ans == []

    # Create a database table
    with sqlite3.connect(expenses.database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS test_a (\n\tid INTEGER PRIMARY KEY AUTOINCREMENT,\n\tname TEXT)")

    ans = expenses.query_existing_database_tables()
    assert 'test_a' in ans

    # Create another database table
    with sqlite3.connect(expenses.database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS test_b (\n\tid INTEGER PRIMARY KEY AUTOINCREMENT,\n\tname TEXT)")

    ans = expenses.query_existing_database_tables()
    assert 'test_b' in ans
    assert 'test_a' in ans


def test_add_expense(provision_expense_database):
    """
    Add an expense
    """
    expenses = provision_expense_database






# def test_create_table(tmp_path):
#     fp = tmp_path / "test.db"
#     assert not os.path.exists(fp)
#     create_table(fp, "test")
#     assert os.path.exists(fp)

# def test_add_row():
#     create_table

# def test_query_all():
#     pass