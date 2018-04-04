from flask import flash, session
from persistance import *
from Subscription import Subscription
from Notification import Notification
from LectureTopic import LectureTopic


def myNotification():
    all_subs = []
    myNot = []
    postToNot = []
    for x in session['user_subsciptions']:
        s = retrieve(Subscription, "LTid", x)
        for b in s:
            if (b.getUser() == session['user_id']):
                all_subs.append(b)
    for sub in all_subs:
        x = retrieve(Notification, "subscription", sub.getSid())
        if len(x) > 0:
            delete(Notification, "Nid", x[0].getNid())
            if sub.getLTid() not in myNot:
                myNot.append(sub.getLTid())

    for x in myNot:
        x = retrieve(LectureTopic, "LTid", x)
        postToNot.append(x[0])
    return postToNot
