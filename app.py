from flask import Flask, render_template

from databases import ExpenseDatabase, IncomesDatabase
from config import EXPENSE_PATH, INCOME_PATH

# Create an instance of the Flask class
app = Flask(__name__)


# Define a route and its associated handler
@app.route("/")
def home():
    # return "Hello, World!"
    return render_template("home.html")


@app.route("/expenses")
def expenses():
    expense_db = ExpenseDatabase(EXPENSE_PATH)
    df = expense_db.query_all_expenses()
    return df.to_html()


@app.route("/incomes")
def incomes():
    income_db = IncomesDatabase(INCOME_PATH)
    df = income_db.query_all_incomes()
    return df.to_html()


# Run the app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
