from flask import Flask, render_template, flash, redirect, url_for, request, session, logging, g
from data import lectures
import sqlite3
import os
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
# from passlib.hash import sha256_crypt
from functools import wraps
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
    with app.open_resource('Schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_submitted = request.form['password']

        db = get_db()
        db.row_factory = sqlite3.Row
        cur = db.cursor()

        cur.execute("SELECT * FROM User WHERE username = ?", [username])
        data = cur.fetchone()
        if data:
            password = data['password']

            # if sha256_crypt.verify(password_submitted, password):
            #    app.logger.info("Login successful")
            if (password_submitted == password):
                session['logged_in'] = True
                return redirect(url_for('home'))
            else:
                error = "Login failed: Incorrect password"
                return render_template('login.html', error= error)

        else:
            error = "Login failed: Username not found"
            return render_template('login.html', error = error)
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', "success")
    return redirect(url_for('login'))


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Please login", "danger")
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@is_logged_in
def home():
    return render_template('home.html')


@app.route('/lectures')
@is_logged_in
def lectures():
    return render_template('lecturesPage.html', lectures = Lectures)


@app.route('/lecture/<string:id>/')
@is_logged_in
def lecture(id):
    return render_template('lecture.html', id = id)


@app.route('/lecture/<string:id>/discussion')
@is_logged_in
def lecture_discussion(id):
    return render_template('discuss.html', id = id)


if __name__ == '__main__':
    app.run()
