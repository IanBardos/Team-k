from wtforms import Form, TextAreaField, validators
from flask import flash, redirect, url_for, session
from persistance import *
from Comment import Comment
from Subscription import Subscription
from Notification import Notification


class postingCForm(Form):
    Body = TextAreaField('Body', [validators.length(min=1, max = 300)])


def postComment(type, form, LTid):
    body = form.Body.data
    # When creating a new comment the 0 for the id is just a place holder because when put into the database we will auto increment the id
    newPost = Comment(0, session['user_id'], body, 0, LTid)
    persist(newPost)
    subscriptions = retrieve(Subscription, "LTid", LTid)

    for subscription in subscriptions:
        newNotification = Notification(0, subscription.getSid())
        persist(newNotification)

    flash('Comment Created', 'success')
    if type == 'Topic':
        return redirect(url_for("topic_discussion", id = LTid))
    elif type == 'Lecture':
        return redirect(url_for("lecture_discussion", id = LTid))
