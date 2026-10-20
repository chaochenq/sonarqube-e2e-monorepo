import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/invoices")
def invoices():
    account = request.args.get("account")
    cursor = sqlite3.connect("billing.db").cursor()
    cursor.execute(f"SELECT id, amount FROM invoices WHERE account = '{account}'")
    return {"invoices": cursor.fetchall()}
