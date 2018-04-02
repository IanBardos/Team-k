class Comment:
    """
    this is comment class for the Topic

    it contains elements of a comment

    Contains parameter:
        Cid -- int -- id to identify the comment (must be unique)
        commenter --  int -- Uid(from class User) -- static -- user that poster the comment
        info -- string -- this is the comment itself
        LTid -- int -- LTid(from class LectureTopic)-- this is the lecture/topic the commment was posted on

    Contain function:
        Comment(commenter, info, Pid)
            ---constructor
        getInfo()
            -- acessor for info
        getLTid()
            -- acessor for LTid
        getCid()
            -- acessor for Cid
        getCommenter()
            -- acessor for commentor
    --- info is the commment
    """
    def __init__(self, Cid, commenter, info, votes, LTid):
        # Cid -- int
        #  commenter -- int
        #  info -- string
        # votes -- int
        # Pid -- int
        self.Cid = Cid
        self.commenter = commenter
        self.info = info
        self.votes = votes
        self.LTid = LTid

    def getInfo(self):
        return self.info

    def getLTid(self):
        return self.LTid

    def getCid(self):
        return self.Cid

    def getCommenter(self):
        return self.commenter

    def getVotes(self):
        return self.votes

    def upVote(self):
        self.votes += 1

    def downVote(self):
        self.votes -= 1
