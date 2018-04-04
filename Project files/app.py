from flask import Flask, render_template, flash, redirect, url_for, request, session, logging, g
import sqlite3
import os
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from functools import wraps
from postingLT import *
from postingComment import *
from persistance import *
from Login_Logout_Handle import *
from User import User
from LectureTopic import LectureTopic
from Comment import Comment
from Subscription import Subscription
from Notification import Notification
# from passlib.hash import sha256_crypt  (not using now, but in futur deploiment would be used for password incryption)
app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, "Project.db"),
    SECRET_KEY = 'Team-k'
))


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


# login page for the app, uses log_in function from Login_Logout_Handle
@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        page = log_in()
        return page
    return render_template('login.html')


# logout page for the app, uses log_out function from Login_Logout_Handle
@app.route('/logout')
def logout():
    page = log_out()
    return page


def is_logged_in(f):
    """is_logged_in function
    function to check weither the user us loged in for the current session, allows for limiting
    access to certain pages to users that are logged in"""
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Please login", "danger")
            return redirect(url_for('login'))
    return wrap


# Home page, checks to see if user is loged in for the session
@app.route('/')
@is_logged_in
def home():
    return render_template('home.html')


# Topics page, checks to see if user is loged in for the session
@app.route('/topics')
@is_logged_in
def topics():
    topics = retrieve(LectureTopic, 'type', 'Topic')
    return render_template('TopicsPage.html', topics = topics)


# Topic page, checks to see if user is loged in for the session
@app.route('/topic/<string:id>/')
@is_logged_in
def topic(id):
    topic = retrieve(LectureTopic, "LTid", id)
    topicUser = retrieve(User, "Uid", topic[0].getCreator())
    return render_template('topic.html', topic = topic[0], user = topicUser[0])


# Topic discusion page, checks to see if user is loged in for the session
@app.route('/topic/<string:id>/discussion')
@is_logged_in
def topic_discussion(id):
    topic = retrieve(LectureTopic, "LTid", id)
    comments = retrieve(Comment, "LTid", id)
    for i in range(len(comments)):
        temp1 = retrieve(User, 'Uid', comments[i].getCommenter())
        temp1 = temp1[0]
        temp = [comments[i], temp1]
        comments[i] = temp
    return render_template('discuss_T.html', topic = topic[0], comments = comments)


# Lectures page, checks to see if user is loged in for the session
@app.route('/lectures')
@is_logged_in
def lectures():
    lectures = retrieve(LectureTopic, 'type', 'Lecture')
    return render_template('lecturesPage.html', lectures = lectures)


# Lecture page, chcecks to see if the user is logged in for the session
@app.route('/lecture/<string:id>/')
@is_logged_in
def lecture(id):
    lecture = retrieve(LectureTopic, "LTid", id)
    lectureUser = retrieve(User, "Uid", lecture[0].getCreator())
    return render_template('lecture.html', lecture = lecture[0], user = lectureUser[0])


# Lecture discusion page, checks to see if user is loged in for the session
@app.route('/lecture/<string:id>/discussion')
@is_logged_in
def lecture_discussion(id):
    lecture = retrieve(LectureTopic, "LTid", id)
    comments = retrieve(Comment, "LTid", id)
    for i in range(len(comments)):
        temp1 = retrieve(User, 'Uid', comments[i].getCommenter())
        temp1 = temp1[0]
        temp = [comments[i], temp1]
        comments[i] = temp
    return render_template('discuss_L.html', lecture = lecture[0], comments = comments)


# add a lecture or a topic, checks to see if user is loged in for the session
@app.route('/add/<string:type>', methods=['GET', 'POST'])
@is_logged_in
def add_topicLecture(type):
    form = postingForm(request.form)
    if request.method == "POST" and form.validate():
        page = postLT(type, form)
        return page
    return render_template("add.html", form = form, type = type)


# edit a lecture or a topic, checks to see if user is loged in for the session
@app.route('/edit/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_topicLecture(id):
    toEdit = retrieve(LectureTopic, "LTid", id)
    toEdit = toEdit[0]
    form = postingForm(request.form)
    form.Title.data = toEdit.getTitle()
    form.Body.data = toEdit.getBody()
    if request.method == "POST" and form.validate():
        page = editLT(form, toEdit)
        return page
    return render_template("edit.html", form = form, toEdit=toEdit)


if __name__ == '__main__':
    app.run()
