"""
Written by b5050d

2.28.2025

Testing script for the databases script
"""

import sqlite3
import pytest
from databases import ExpenseDatabase, IncomesDatabase


@pytest.fixture()
def provision_expense_database(tmp_path):
    fp = tmp_path / "test.db"
    return ExpenseDatabase(fp)


@pytest.fixture()
def provision_income_database(tmp_path):
    """"""
    fp = tmp_path / "test.db"
    return IncomesDatabase(fp)


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
        table_create = "CREATE TABLE IF NOT EXISTS"
        values = "(\n\tid INTEGER PRIMARY KEY AUTOINCREMENT,\n\tname TEXT)"
        cursor.execute(f"{table_create} test_a {values}")

    ans = expenses.query_existing_database_tables()
    assert "test_a" in ans

    # Create another database table
    with sqlite3.connect(expenses.database_path) as connection:
        cursor = connection.cursor()
        table_create = "CREATE TABLE IF NOT EXISTS"
        values = "(\n\tid INTEGER PRIMARY KEY AUTOINCREMENT,\n\tname TEXT)"
        cursor.execute(f"{table_create} test_b {values}")

    ans = expenses.query_existing_database_tables()
    assert "test_b" in ans
    assert "test_a" in ans


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
    date = "2024/07/21"
    expenses.add_expense(category, source, amount, date)


def test_query_all_expenses(provision_expense_database):
    """
    Add an expense
    """
    expenses = provision_expense_database
    expenses.create_table()

    category = "Housing"
    source = "Rent"
    amount = 1699.99
    date = "2024/07/21"
    expenses.add_expense(category, source, amount, date)

    df = expenses.query_all_expenses()
    # Get the first row of a dataframe as a dict
    first_row = df.iloc[0].to_dict()

    assert first_row["category"] == "Housing"
    assert first_row["source"] == "Rent"
    assert first_row["amount"] == 1699.99
    assert first_row["date"] == date


def test_income_init(provision_income_database):
    incomes = provision_income_database
    assert incomes.database_path


def test_income_create_table(provision_income_database):
    incomes = provision_income_database
    ans = incomes.query_existing_database_tables()
    assert ans == []
    incomes.create_table()
    ans = incomes.query_existing_database_tables()
    assert "incomes" in ans


def test_add_income(provision_income_database):
    """
    Add an income
    """
    incomes = provision_income_database
    incomes.create_table()

    category = "Work"
    source = "AgileRF"
    amount = 2001.69
    date = "2024/07/21"
    incomes.add_income(category, source, amount, date)


def test_query_all_incomes(provision_income_database):
    """ """
    incomes = provision_income_database
    incomes.create_table()

    category = "Work"
    source = "AgileRF"
    amount = 2001.69
    date = "2024/07/21"
    incomes.add_income(category, source, amount, date)

    df = incomes.query_all_incomes()
    # Get the first row of a dataframe as a dict
    first_row = df.iloc[0].to_dict()

    assert first_row["category"] == "Work"
    assert first_row["source"] == "AgileRF"
    assert first_row["amount"] == 2001.69
    assert first_row["date"] == date
