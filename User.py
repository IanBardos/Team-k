class User:
    """
    this is user class for the program
    
    it contains infomation of each user

    Contain parameters:
        name -- string
        password -- string
        munId -- string -- static
        gender -- string
        logedIn -- boolean
        picFile -- string

    Contain functions:
        constractor
        accessor for all parameter
        mutator for non-static parameter
        
    ---logedIn state if a user is loged in
    
    ---a user can be a professor or a student

    ---picfile is the address(in database) of the profile picture user uploaded
    
    ---mandatory parameters: name, password, munId

    ---more parameter may be added
    """
    def __init__(self, name, passward, munId):
        ## name -- string
        ## password -- string
        ## munId -- string
        self.name = name
        self.password = password
        self.munId = munId

##----------munId----------------------
    def getmunId(self):
        return self.munId

##----------name----------------------
    def setName(self, name):
        ## name -- string
        self.name = name

    def getName(self):
        return self.name
    
##----------password--------------------Question
    def setPassword(self, password):
        ## password -- string
        self.password = password

    def getPassword(self):
        return self.password
    
##----------gender----------------------    
    def setGender(self, gender):
        ## gender -- string
        self.gender = gender
        
    def getGender(self):
        return self.gender

##----------logedIn----------------------    
    def setLogin(self, logedIn):
        ## logedIn -- boolean
        self.logedIn = logedIn

    def getLogin(self):
        return self.logedIn
    
##----------picFile----------------------    
    def setPicFile(self, picFile):
        ## picFile -- string
        self.picFile = picFile

    def getPicFile(self):
        return self.picFile

