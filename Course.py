class Course:
    """
    this is course class for the program

    it contains information of each course

    Contain parameters:
        name -- string -- static
        admin -- user(User.py) -- static
        term -- string -- static
        topic[] -- Topic(Topic.py)

    Contain functions:
        constractor
        addTopic(topic1)
            ---topic1 -- Topic(Topic.py)
            ---add topic1 in to self.topic[]
            
        getTopic(index)
            ---index -- int
            ---read topic from self.topic[]
            ---leave index empty to get latest topic

        removeTopic(index)
            ---index -- int
            ---remove the topic at index


    
    ---name state which course this is
        e.g. cs2005
    
    ---admin should be a professor (User)

    ---term states in which semaster this course is in
        e.g. winter_2017-2018
    
    ---mandatory parameters: name, admin, term
    """
    def __init__(self, name, admin, term):
        ## name -- string
        ## admin -- user(User.py)
        ## term -- string
        self.name = name
        self.admin = admin
        self.term = term
        self.topic = []

    def addTopic(self,topic):
        ## topic -- Topic(Topic.py)
        self.topic.append(topic)

    def getTopic(self, index = -1):
        return self.topic[index]

        
    def removeTopic(self,index):
        ## index -- int
        self.topic.remove[index]
                
