"""Persistence module for project

Objects are persisted using the persist function.  Object are retrieved from
the database witht he retrieve function. The client module(s) need to use
backup/load when the state of the system is critical, so data is not lost.

Functions:

    backup - immediately backup all objects marked for persistence (not yet implemented)
    load - recover persisted objects from backup (not yet implemented)
    persist - record an object for persistence
    retrieve - get a list of persisted objects using optional criteria

Examples:

    Persist student objects:
        >>> a = User("iwbardos", "123097", 1)
        >>> b = User("Test", "12345", 2)
        >>> persist(a)
        User("iwbardos", "123097", 1)
        >>> persist(b)
        User("Test", "12345", 2)
        >>> backup()
        >>> load()
        >>> retrieve(Student)
        [User("iwbardos", "123097", 1), User("Test", "12345", 2)]
        >>> retrieve(Student, 'username', 'iwbardos') # object a has an attribute 'username'
        [User("iwbardos", "123097", 1)]

"""

from User import User
from LectureTopic import LectureTopic
from Comment import Comment
from Subscription import Subscription
from Notification import Notification
import sqlite3

__all__ = ['persist', 'backup', 'load', 'retrieve', 'update', 'delete']

__defaultfile = "Project.db"


# object-relational mappers for each class type
class _UserORM:

    schema = """drop table if exists User;
    create table User (
      Uid integer primary key autoincrement,
      username text not null,
      password text not null
    );"""

    @staticmethod
    def sql_id(obj):
        return obj.getUid()

    @staticmethod
    def sql_reset(conn):
        conn.cursor().executescript(_UserORM.schema)

    @staticmethod
    def sql_persist(conn, obj):
        conn.execute("INSERT INTO User (username, password) VALUES (?, ?)", [obj.getUsername(), obj.getPassword()])

    @staticmethod
    def sql_retrieve(conn, searchfield=None, searchval=None):
        conn.row_factory = sqlite3.Row
        if searchfield:
            cur = conn.execute('SELECT * FROM User WHERE "{}"="{}"'.format(searchfield, searchval))
        else:
            cur = conn.execute('SELECT * FROM User')

        # construct the object
        results = []
        for tablerow in cur.fetchall():
            newobj = User(tablerow['username'], tablerow['password'], tablerow['Uid'])
            results.append(newobj)
        return results


class _LectureTopicORM:
    schema = """drop table if exists LecturesTopics;
    create table LecturesTopics(
      LTid integer primary key autoincrement,
      type text not null,
      Title text not null,
      Body text not null,
      Author integer not null,
      FOREIGN KEY (Author) REFERENCES user(Uid)
      );"""

    @staticmethod
    def sql_id(obj):
        return obj.getLTid()

    @staticmethod
    def sql_reset(conn):
        conn.cursor().executescript(_LectureTopicORM.schema)

    @staticmethod
    def sql_persist(conn, obj):
        conn.execute('INSERT INTO LecturesTopics  (type, Title, Body,Author) values (?, ?, ?, ?)', [obj.getType(), obj.getTitle(), obj.getBody(), obj.getCreator()])

    @staticmethod
    def sql_update(conn, obj):
        conn.execute('UPDATE LecturesTopics SET Title=?, Body=? WHERE LTid = ?', [obj.getTitle(), obj.getBody(), obj.getLTid()])

    @staticmethod
    def sql_delete(conn, searchfield, searchval):
        conn.execute('DELETE FROM LecturesTopics WHERE "{}" = "{}"' .format(searchfield, searchval))

    @staticmethod
    def sql_retrieve(conn, searchfield=None, searchval=None):
        conn.row_factory = sqlite3.Row
        if searchfield:
            cur = conn.execute('SELECT * FROM LecturesTopics WHERE "{}"="{}"'.format(searchfield, searchval))
        else:
            cur = conn.execute('SELECT * FROM LecturesTopics')

        # construct the object
        results = []
        for tablerow in cur.fetchall():
            newobj = LectureTopic(tablerow['LTid'], tablerow['Title'], tablerow['Author'], tablerow['type'], tablerow['Body'])
            results.append(newobj)
        return results


class _CommentORM:
    schema = """drop table if exists Comments;
    create table Comments(
      Cid integer primary key autoincrement,
      Author int not null,
      Body text not null,
      votes integer not null,
      LTid int not null,
      FOREIGN KEY (Author) REFERENCES user(Uid),
      FOREIGN KEY (LTid) REFERENCES LecturesTopics(LTid)
    );"""

    @staticmethod
    def sql_id(obj):
        return obj.getCid()

    @staticmethod
    def sql_reset(conn):
        conn.cursor().executescript(_CommentORM.schema)

    @staticmethod
    def sql_persist(conn, obj):
        conn.execute('INSERT INTO Comments  (Author, Body, votes, LTid) values (?, ?, ?, ?)', [obj.getCommenter(), obj.getInfo(), obj.getVotes(), obj.getLTid()])

    @staticmethod
    def sql_retrieve(conn, searchfield=None, searchval=None):
        conn.row_factory = sqlite3.Row
        if searchfield:
            cur = conn.execute('SELECT * FROM Comments WHERE "{}"="{}"'.format(searchfield, searchval))
        else:
            cur = conn.execute('SELECT * from Comments')

        # construct the object
        results = []
        for tablerow in cur.fetchall():
            newobj = Comment(tablerow['Cid'], tablerow['Author'], tablerow['Body'], tablerow['votes'], tablerow['LTid'])
            results.append(newobj)
        return results

    @staticmethod
    def sql_update(conn, obj):
        conn.execute('UPDATE Comments SET votes=? WHERE Cid = ?', [obj.getVotes(), obj.getCid()])


class _SubcriptionORM:
    schema = """drop table if exists Subcriptions;
    create table Subscriptions(
      Sid integer primary key autoincrement,
      user integer not null,
      LTid integer not null,
      FOREIGN KEY (user) REFERENCES user(Uid),
      FOREIGN KEY (LTid) REFERENCES LecturesTopics(LTid)
    );"""

    @staticmethod
    def sql_id(obj):
        return obj.getSid()

    @staticmethod
    def sql_reset(conn):
        conn.cursor().executescript(_SubcriptionORM.schema)

    @staticmethod
    def sql_persist(conn, obj):
        conn.execute('INSERT INTO Subscriptions  (user, LTid) values (?, ?)', [obj.getUser(), obj.getLTid()])

    @staticmethod
    def sql_retrieve(conn, searchfield=None, searchval=None):
        conn.row_factory = sqlite3.Row
        if searchfield:
            cur = conn.execute('SELECT * FROM Subscriptions WHERE "{}"="{}"'.format(searchfield, searchval))
        else:
            cur = conn.execute('SELECT * from Subscriptions')

        # construct the object
        results = []
        for tablerow in cur.fetchall():
            newobj = Subscription(tablerow['Sid'], tablerow['LTid'], tablerow['user'])
            results.append(newobj)
        return results

    @staticmethod
    def sql_delete(conn, searchfield, searchval):
        conn.execute('DELETE FROM Subscriptions WHERE "{}" = "{}"' .format(searchfield, searchval))


class _NotificationORM:
    schema = """drop table if exists Notification;
    create table Notification(
      Nid integer primary key not null,
      subscription integer not null,
      FOREIGN KEY (subscription) REFERENCES Subscriptions(Sid)
    );"""

    @staticmethod
    def sql_id(obj):
        return obj.getNid()

    @staticmethod
    def sql_reset(conn):
        conn.cursor().executescript(_SubcriptionORM.schema)

    @staticmethod
    def sql_persist(conn, obj):
        conn.execute('INSERT INTO Notification  (subscription) values (?)', [obj.getSubcription()])

    @staticmethod
    def sql_retrieve(conn, searchfield=None, searchval=None):
        conn.row_factory = sqlite3.Row
        if searchfield:
            cur = conn.execute('SELECT * FROM Notification WHERE "{}"="{}"'.format(searchfield, searchval))
        else:
            cur = conn.execute('SELECT * from Notification')

        # construct the object
        results = []
        for tablerow in cur.fetchall():
            newobj = Notification(tablerow['Nid'], tablerow['subscription'])
            results.append(newobj)
        return results

    @staticmethod
    def sql_delete(conn, searchfield, searchval):
        conn.execute('DELETE FROM Notification WHERE "{}" = "{}"' .format(searchfield, searchval))


# lookup dictionary for class-table mappers
orms = {
    'User': _UserORM,
    'LectureTopic': _LectureTopicORM,
    'Comment': _CommentORM,
    'Subscription': _SubcriptionORM,
    'Notification': _NotificationORM
}


# exported functions follow below
def backup(storefileName=__defaultfile):
    """Recover persisted objects from backup

       Placeholder for future; possible cache update?
       Parameters
            storefileName - change the backup file (for testing)
    """
    pass


def load(storefile=__defaultfile):
    """Load persisted objects from backup file

      Placeholder for future; possible cache recovery?
      Parameters
            storefileName - change the backup file (for testing)
    """
    pass


def _reset():
    """wipe the default backup file and persistent list
    for testing purposes, reads in from the Schema.sql file to restore the database"""
    conn = sqlite3.connect(__defaultfile)
    conn.cursor().executescript("Schema.sql")
    conn.commit()
    backup()
    conn.close()


def persist(o):
    """Persist the object o

       returns: a persistent version of the object; if an equivalent object
                is already persisted, you get the persisted object back
    """
    orm = orms[o.__class__.__name__]  # lookup the correct orm for this class
    conn = sqlite3.connect(__defaultfile)
    orm.sql_persist(conn, o)
    conn.commit()
    conn.close()
    return o


def update(o):
    """Updates the object o

       returns: a updated version of the object
    """
    orm = orms[o.__class__.__name__]  # lookup the correct orm for this class
    conn = sqlite3.connect(__defaultfile)
    orm.sql_update(conn, o)
    conn.commit()
    conn.close()
    return o


def delete(clss, searchattr, searchvalue):
    """Deletes a persisted objects using criteria

       parameters:
            clss - the class of the objects to retrieve
            searchattr -- attribute name to find object to delete
            searchval -- value to find object to delete
       returns: object that was deleted
    """
    orm = orms[clss.__name__]  # lookup the correct orm for this class
    conn = sqlite3.connect(__defaultfile)
    o = orm.sql_delete(conn, searchattr, searchvalue)
    conn.commit()
    conn.close()
    return o


def retrieve(clss, searchattr=None, searchvalue=None):
    """Get a list of persisted objects using optional criteria

       parameters:
            clss - the class of the objects to retrieve
            searchattr - optional attribute name to limit retrieval
            searchval - optional value to limit retrieval. required if
                        searchattr is present.
       returns: a list of the retrieved objects
    """
    orm = orms[clss.__name__]  # lookup the correct orm for this class
    conn = sqlite3.connect(__defaultfile)
    matches = orm.sql_retrieve(conn, searchattr, searchvalue)
    conn.commit()
    conn.close()
    return matches
