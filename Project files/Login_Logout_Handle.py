"""Login_Logout_Handle module for Project

User is loged in to the system using the log_in function. User is loged out using the logout functions

Functions:

    log_in: logs in the user using the login infromation submited from the form of the login page
    returns the home page to be rendered in the app
    log_out: logs out the user by clearing the session and returning the login page to be rendered by the app
"""

from flask import render_template, redirect, url_for, request, session, flash
from User import User
from Subscription import Subscription
from persistance import *


def log_in():
    """log_in function
    *If matching user(match by username from database) is found and password matches, flash success message,
    sets the session information of the user and return home page to be rendered by app
    *If matching user (match by username from database) is found but password incorrect,
        flash error message to say password incorrect and return login page to be rendered by app
    *If no matching user found (match by username from database), flash error message to say
        user not found and return login page to be rendered

    username -- string taken from form on the login page
    password_submitted -- string taken from form on the login page

    data -- the matching user from the database, retrieved with the persistance module
    password -- password retrieved for the user to be matched against password_submitted
    """
    username = request.form['username']
    password_submitted = request.form['password']

    data = retrieve(User, "username", username)

    if len(data) > 0:
        data = data[0]
        password = data.getPassword()

        # if sha256_crypt.verify(password_submitted, password):
        #    app.logger.info("Login successful")
        if (password_submitted == password):
            session['logged_in'] = True
            session['user_id'] = data.getUid()
            session['username'] = data.getUsername()
            subObjects = retrieve(Subscription, "User", data.getUid())
            session['user_subsciptions'] = []
            for sub in subObjects:
                session['user_subsciptions'].append(sub.getLTid())
            flash("You are now logged in", "success")
            return redirect(url_for('home'))
        else:
            error = "Login failed: Incorrect password"
            return render_template('login.html', error= error)

    else:
        error = "Login failed: Username not found"
        return render_template('login.html', error = error)


def log_out():
    """log_out function

    *clears the current session, flashes logout success message and returns login page to be rendered
    """
    session.clear()
    flash('You are now logged out', "success")
    return redirect(url_for('login'))
