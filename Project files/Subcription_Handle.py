from Subscription import Subscription
from persistance import *
from flask import session, redirect, flash, url_for


def sub(type, id):
    newSub = Subscription(0, id, session['user_id'])
    persist(newSub)
    session['user_subsciptions'].append(eval(id))
    flash("You are now subscibed", "success")
    if type == 'Topic':
        return redirect(url_for("topic_discussion", id = id))
    elif type == 'Lecture':
        return redirect(url_for("lecture_discussion", id = id))


def unsub(type, id):
    sub = retrieve(Subscription, "LTid", id)
    subUid = []
    for s in sub:
        subUid.append(s.getUser())
    i = subUid.index(session['user_id'])
    toUnsub = sub[i]
    delete(Subscription, "Sid", toUnsub.getSid())
    session['user_subsciptions'].remove(eval(id))
    flash("You are now unsubscibed", "success")
    if type == 'Topic':
        return redirect(url_for("topic_discussion", id = id))
    elif type == 'Lecture':
        return redirect(url_for("lecture_discussion", id = id))
