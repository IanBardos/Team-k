from wtforms import Form, StringField, TextAreaField, validators
from flask import Flask, render_template, flash, redirect, url_for, request, session, logging, g
from persistance import *
from Comment import Comment
from Subscription import Subscription
from Notification import Notification
from User import User


class postingCForm(Form):
    Body = TextAreaField('Body', [validators.length(min=1, max = 300)])
