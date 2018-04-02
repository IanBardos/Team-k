class LectureTopic:
    """
    this is lecture and topic class for Course

    it contains elements of a lecture or topic

    Contain parameter:
        LTid -- int -- id to identify the Lecture/topic (must be unique)
        title -- string -- static
        creator -- User(User.py) --static
        type -- string -- static
        body -- string


    Contain function:
        LectureTopic(title,creator,type,body)
            --- constructor
        --- acessor methods for attributes
        getLTid(self)
        getTitle(self)
        getCreator(self)
        getType(self)
        getBody(self)
    """

    def __init__(self, LTid, title, creator, type, body):
        # LTid -- int
        # title -- string
        # creator -- int -- Uid
        # type -- string
        # body -- string
        self.LTid = LTid
        self.title = title
        self.creator = creator
        self.type = type
        self.body = body

    def getLTid(self):
        return self.LTid

    def getTitle(self):
        return self.title

    def getCreator(self):
        return self.creator

    def getType(self):
        return self.type

    def getBody(self):
        return self.body

    def setBody(self, new):
        self.Body = new
