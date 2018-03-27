from flask import Flask, render_template, flash, redirect, url_for, request, session, logging, g
from data import lectures
import sqlite3
import os
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, "Project.db"),
    SECRET_KEY = 'Team-k'
))

Lectures = lectures()


def connect_db():
    """Connects to the specific database."""
    db = sqlite3.connect(app.config["DATABASE"])
    db.row_factory = sqlite3.Row
    return db


def get_db():
    """Opens a new database connection if there is none yet for the
     current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request"""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database"""
    init_db()
    print('Datebase Initialized')


def init_db():
    db = get_db()
    with app.open_resourcce('Schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_submited = request.form['password']

        db = get_db()
        cur = db.cursor()

        result = cur.execute("SELECT * FROM User WHERE username = ?", [username])
        if result:
            data = cur.fetchone()
            password = data['password']

            if sha256_crypt.verify(password_submited, password):
                app.logger.info("Login successful")
        else:
            app.logger.inf('No user')
    return render_template ('login.html')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/lectures')
def lectures():
    return render_template('lecturesPage.html', lectures = Lectures)


@app.route('/lecture/<string:id>/')
def lecture(id):
    return render_template('lecture.html', id = id)


@app.route('/lecture/<string:id>/discussion')
def lecture_discussion(id):
    return render_template('discuss.html', id = id)


if __name__ == '__main__':
    app.run()
