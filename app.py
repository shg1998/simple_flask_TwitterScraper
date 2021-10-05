import sqlite3
from sqlite3.dbapi2 import connect
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    # connection to db
    connection = sqlite3.connect('shg_followers.db')
    curs = connection.cursor()

    try:
        records = curs.execute('select * from shg_stats').fetchall()
    except Exception:
        records = []

    return render_template('stats.html',records=records)