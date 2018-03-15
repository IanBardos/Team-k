class Topic:
    """
    this is topic class for Course

    it contains elements of a topic

    Contain parameter:
        title -- string -- static
        creator -- User(User.py) --static
        comment[] -- Comment(Comment.py)

    Contain function:
        Topic(title,creator,course)
            ---constructor
        getTitle()
        getCreator()
        addComment(comment1)
            ---comment1 -- Comment(Comment.py)
            ---add comment1 to self.comment[]
        getComment(index)
            ---index -- int
        removeComment(index)
            ---index -- int

    """

    def __init__(self, title, creator, course):
        ## title -- string
        ## creator -- User(User.py)
        ## comment -- Comment(Comment.py)
        self.title = title
        self.creator = creator
        self.comment = []


    def getTitle(self):
        return self.title


    def getCreator(self):
        return self.creator

    
    def addComment(self,sComment):
        ## topic -- Topic(Topic.py)
        self.comment.append(sComment)

    def getComment(self,index = -1):
        ## index -- int
        return self.comment[index]


    def removeComment(self,index):
        ## index -- int
        self.comment.remove[index]
