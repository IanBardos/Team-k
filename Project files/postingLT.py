from wtforms import Form, StringField, TextAreaField, validators
from flask import flash, redirect, url_for, session, request
from persistance import *
from LectureTopic import LectureTopic


class postingForm(Form):
    Title = StringField('Title', [validators.length(min=1, max=200)])
    Body = TextAreaField('Body', [validators.length(min=1)])


def postLT(type, form):
    title = form.Title.data
    body = form.Body.data
    # When creating a new lecture/topic the 0 for the id is just a place holder because when put into the database we will auto increment the id
    newPost = LectureTopic(0, title, session['user_id'], type, body)
    persist(newPost)

    if type == 'Topic':
        flash('Topic Created', 'success')
        return redirect(url_for('topics'))
    elif type == 'Lecture':
        flash('Lecture Created', 'success')
        return redirect(url_for('lectures'))


def editLT(form, toEdit):
    title = request.form['Title']
    body = request.form['Body']
    editedPost = LectureTopic(toEdit.getLTid(), title, toEdit.getCreator(), toEdit.getType(), body)
    update(editedPost)

    if toEdit.getType() == 'Topic':
        flash('Topic Edited', 'success')
        return redirect(url_for('topics'))
    elif toEdit.getType() == 'Lecture':
        flash('Lecture Edited', 'success')
        return redirect(url_for('lectures'))
