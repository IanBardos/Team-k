import unittest

from User import User
from LectureTopic import LectureTopic
from Comment import Comment
from Subscription import Subscription
from Notification import Notification
from persistance import *

class Test(unittest.TestCase):
    
    def setUp(self):        
        self.student = User("user", "password", 1)
        self.lecture = LectureTopic(1, "L1", "author", "Lecture", "info")
        self.comment = Comment(1, "author", "info", 2, self.lecture.getLTid())
        self.subscribe = Subscription(1, self.lecture.getLTid(), self.student.getUid())
        self.notify = Notification(1, self.subscribe.getSid())

    """
    User.py TESTS
    """

    def test_getUid(self):
        self.assertEqual(self.student.getUid(), 1)

    def test_getUsername(self):
        self.assertEqual(self.student.getUsername(), "user")

    def test_getPassword(self):
        self.assertEqual(self.student.getPassword(), "password")

    """
    LectureTopic.py TESTS
    """
    def test_getLTid(self):
        self.assertEqual(self.lecture.getLTid(), 1)

    def test_getTitle(self):
        self.assertEqual(self.lecture.getTitle(), "L1")

    def test_getCreator(self):
        self.assertEqual(self.lecture.getCreator(), "author")

    def test_getType(self):
        self.assertEqual(self.lecture.getType(), "Lecture")

    def test_getBody(self):
        self.assertEqual(self.lecture.getBody(), "info")

    def test_setBody(self):
        self.lecture.setBody("new info")
        self.assertEqual(self.lecture.getBody(), "new info")
    """
    Comment.py TESTS
    getLTid()  is tested in LectureTopic.py tests
    """
    
    def test_getInfo(self):
        self.assertEqual(self.comment.getInfo(), "info")

    def test_getLTid(self):
        self.assertEqual(self.lecture.getLTid(), 1)

    def test_getCid(self):
        self.assertEqual(self.comment.getCid(), 1)

    def test_getCommenter(self):
        self.assertEqual(self.comment.getCommenter(), "author")

    def test_getVotes(self):
        self.assertEqual(self.comment.getVotes(), 2)

    def test_upVote(self):
        self.comment.upVote()
        self.assertEqual(self.comment.getVotes(), 3)

    def test_downVote(self):
        self.comment.downVote()
        self.assertEqual(self.comment.getVotes(), 1)

    """
    Subscription.py TESTS
    getLTid()  is tested in LectureTopic.py tests
    getUid() is tested in User.py tests
    """
    
    def test_getSid(self):
        self.assertEqual(self.subscribe.getSid(), 1)

    """
    Notification.py TESTS
    getSid() is tested in Subsription.py tests
    """
    
    def test_getNid(self):
        self.assertEqual(self.notify.getNid(), 1) 

    
    """
    User persistance.py TESTS
    """

    def test_persist_user(self):
        persisted = persist(self.student)
        self.assertEqual(persisted, self.student)

    def test_retrieve_user(self):
        retrieved = retrieve(User)
        self.assertEqual(retrieved, self.student)

    """
    LectureTopic persistance.py TESTS
    """

    def test_persist_LT(self):
        persisted = persist(self.lecture)
        self.assertEqual(persisted, self.lecture)

   # def test_update_LT(self):
        #WRITE UPDATE TEST
   
    def test_retrieve_LT(self):
        retrieved = retrieve(LectureTopic)
        self.assertEqual(retrieved, self.lecture)

    def test_delete_LT(self):
        deleted = delete(LectureTopic, "Title", "L1")
        self.assertEqual(deleted, None)

    """
    Comment persistance.py TESTS
    """

    def test_persist_comment(self):
        persisted = persist(self.comment)
        self.assertEqual(persisted, self.comment)

   # def test_update_comment(self):
        #WRITE UPDATE TEST
   
    def test_retrieve_comment(self):
        retrieved = retrieve(Comment)
        self.assertEqual(retrieved, self.comment)

    """
    Subscription persistance.py TESTS
    """

    def test_persist_sub(self):
        persisted = persist(self.subscribe)
        self.assertEqual(persisted, self.subscribe)
   
    def test_retrieve_sub(self):
        retrieved = retrieve(Subscription)
        self.assertEqual(retrieved, self.subscribe)

    def test_delete_sub(self):
        deleted = delete(Subscription, "Sid", 1)
        self.assertEqual(deleted, None)

        
if __name__ == '__main__':
    unittest.main()
