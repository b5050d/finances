"""
Script to handle the incoming data
"""

import os
import pandas as pd
from config import INCOME_PATH, EXPENSE_PATH
from databases import IncomesDatabase, ExpenseDatabase


def ingest_chase_data(data_path):
    """
    Ingest data from a Chase csv file
    """
    # TODO - fix the column misalignment of the chase csv's when
    # loading with pandas

    # TODO - Make sure not to add the same data multiple times

    assert os.path.exists(data_path)
    df = pd.read_csv(data_path)

    # Alright now clean the data and add them to the database
    print(df.head())

    # df.itertuples(index = False)
    print(df.itertuples(index=False).__next__()._fields)

    income_db = IncomesDatabase(INCOME_PATH)
    if not income_db.does_database_exist():
        income_db.create_table()
    expense_db = ExpenseDatabase(EXPENSE_PATH)
    if not expense_db.does_database_exist():
        expense_db.create_table()

    for row in df.itertuples(index=False):
        # print(getattr(row, "_1"))
        # print(row.Details) # For some reason the chase csvs are offset by 1
        date = row.Details
        amount = row.Description
        # TODO - find a way to infer category and source
        category = "NaN"
        source = "NaN"

        # input(type(amount))
        if amount > 0:
            income_db.add_income(category, source, amount, date)
        else:
            expense_db.add_expense(category, source, amount, date)


def ingest_discover_data(discover_path):
    """
    Process Data from my discover card
    """


if __name__ == "__main__":
    cfp = r"C:\Users\b5050d\Workspace\finances\data\chase_sample.CSV"
    ingest_chase_data(cfp)
