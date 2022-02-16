from flask import Flask, render_template
import os
import sqlite3 as sql

app = Flask(__name__)

context = {}

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', context=context)

@app.route("/home/", methods=['GET'])
def home():
    return index()

@app.route("/dashboard/", methods=['GET'])
def dashboard():
    return render_template('dashboard.html', context=context)

def add_data(title, content):
    try:
        # Connecting to database
        con = sql.connect('maria.db')
        # getting cursor
        c = con.cursor()
        # add data
        c.execute(f"INSERT INTO Meals (title, content) VALUSE({title}, {content})")
        # applying the changes
        con.commit()
        return True
    except:
        return False

if __name__ == "__main__":
     port = int(os.environ.get('PORT', 5000))
     app.run(debug=True, host='0.0.0.0', port=port)