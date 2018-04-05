import unittest

class Test(unittest.TestCase):
    
    def setUp(self):        
        self.student = User("user", "password", 1)
        self.lecture = LectureTopic(1, "L1", "author", "Lecture", "info")
        self.comment = Comment(1, "author", "info", 2, self.lecture.getLTid())
        self.subscribe = Subscription(1, self.lecture.getLTid(), self.student.getUid())
        self.notify = Notificaiton(1, self.subscribe.getSid())

    """
    User.py TESTS
    """

    def test_getUid(self):
        self.assertEqual(self.student.getUid(), 1)

    def test_getUsername(self):
        self.assertEqual(self.student.getUsername(), "username")

    def test_getPassword(self):
        self.assertEqual(self.student.getPassword(), "password")

    """
    LectureTopic.py TESTS
    """
    def test_getLTid(self):
        self.assertEqual(self.lecture.getLTid(), 1)

    def test_getTitle(self):
        self.assertEqual(self.lecture.getTitle, "L1")

    def test_getCreator(self):
        self.assertEqual(self.lecture.getCreator(), "author")

    def test_getType(self):
        self.assertEqual(self.lecture.getType(), "Lecture")

    def test_getBody(self):
        self.assertEqual(self.lecture.getBody(), "info")

    def test_setBody(self):
        self.lecture.setBody("new info")
        self.assertEqual(self.lecture.getInfo(), "new info")
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
        self.assertEqual(self.commment.getVotes(), 2)

    def test_upVote(self):
        self.assertEqual(self.commment.upVote(), 3)

    def test_downVote(self):
        self.assertEqual(self.commment.downVote(), 2)

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
    PERSISTANCE TESTS
    persistance.py
    """

    def test_persist_student(self):
        persisted = persist(self.student)
        self.assertEqual(persisted, self.student)

    def test_update_student(self):
        #WRITE UPDATE TEST
    def test_retrieve_student(self):
        retrieved = retrieve(User, "username", "user")
        self.assertEqual(retrieved, self.student)

    def test_delete_student(self):
        deleted = delete(User, "username", "user")
        self.assertEqual(deleted, None)
