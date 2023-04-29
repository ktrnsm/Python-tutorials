#*business follow up
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

conn = sqlite3.connect('sample.db')

c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
conn.commit()


