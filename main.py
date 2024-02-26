from flask import Flask, render_template, request, redirect, url_for
from config import women
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
  conn = get_db_connection()
  WOMANIZER_YO = conn.execute("SELECT * FROM women").fetchall()
  conn.close()
  return render_template('index.html')

@app.route("/women")
def a():
  return render_template("women.html")

@app.route("/men")
def b():
  return render_template("men.html")

@app.route('/woman/<woman_id>')
def show_woman(woman_id):
  conn = get_db_connection
  woman = conn.execute("SELECT woman.*, users.name AS user_name FROM woman LEFT JOIN users WHERE woman.user_id = users.id AND woman.id = ?",(woman_id)).fetchone()
  conn.close()
  return render_template('show_woman.html', woman=woman, WOMANIZER_YO=WOMANIZER_YO)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

def get_db_connection():
  conn = sqlite3.connect('database.db')
  conn.row_factory = sqlite3.Row
  return conn

app.run(host='0.0.0.0', port=81)
