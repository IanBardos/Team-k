from Comment import Comment
from persistance import *
from flask import redirect, url_for


def uVote(type, id, Cid):
    toVote = retrieve(Comment, "Cid", Cid)
    toVote[0].upVote()
    update(toVote[0])
    if type == 'Topic':
        return redirect(url_for("topic_discussion", id = id))
    elif type == 'Lecture':
        return redirect(url_for("lecture_discussion", id = id))


def dVote(type, id, Cid):
    toVote = retrieve(Comment, "Cid", Cid)
    toVote[0].downVote()
    update(toVote[0])
    if type == 'Topic':
        return redirect(url_for("topic_discussion", id = id))
    elif type == 'Lecture':
        return redirect(url_for("lecture_discussion", id = id))
