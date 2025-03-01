"""
Written by b5050d

2.28.2025

Testing script for the databases script
"""

import pytest
import os

from databases import ExpenseDatabase
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

def test_expense_create_table(provision_expense_database):
    expenses = provision_expense_database
    ans = expenses.query_existing_database_tables()
    assert ans == []
    expenses.create_table()
    ans = expenses.query_existing_database_tables()
    assert "expenses" in ans

def test_add_expense(provision_expense_database):
    """
    Add an expense
    """
    expenses = provision_expense_database
    expenses.create_table()

    category = "Housing"
    source = "Rent"
    amount = 1699.99
    expenses.add_expense(category, source, amount)

def test_query_all_expenses(provision_expense_database):
    """
    Add an expense
    """
    expenses = provision_expense_database
    expenses.create_table()

    category = "Housing"
    source = "Rent"
    amount = 1699.99
    expenses.add_expense(category, source, amount)

    df = expenses.query_all_expenses()
    # Get the first row of a dataframe as a dict
    first_row = df.iloc[0].to_dict()

    assert first_row["category"] == "Housing"
    assert first_row["source"] == "Rent"
    assert first_row["amount"] == 1699.99

