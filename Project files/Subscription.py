class Subscription:
    """
    this is subcription class for Course

    it contains elements of a Post

    Contain parameter:
        Sid -- int -- id to identify the Subcription (must be unique) -- static
        LTid -- int -- LTid (from LectureTopic class) -- static -- Lecture/topic the user is subcribed to
        user --  int -- Uid(from class User) -- static -- user that has the subscription

    Contain function:
        Subcription(Sid, LTid, user)
            --- constructor
        --- acessor methods for attributes
        getSid(self)
        getLTid(self)
        getUser(self)
    """

    def __init__(self, Sid, LTid, user):
        # Sid -- int
        # LTid -- int -- LTid
        # user -- int -- Uid
        self.Sid = Sid
        self.LTid = LTid
        self.user = user

    def getSid(self):
        return self.Sid

    def getLTid(self):
        return self.LTid

    def getUser(self):
        return self.user
