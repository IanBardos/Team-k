class User:
    """
    this is user class for the program

    it contains infomation of each user

    Contain parameters:
        Uid -- integer -- static -- id to identify the User (must be unique)
        password -- string -- static
        username -- string -- static

    Contain functions:
        constractor
        accessor for all parameter

    ---more parameter may be added
    """

    def __init__(self, username, password, Uid):
        # name -- string
        # munId -- string
        self.username = username
        self.password = password
        self.Uid = Uid

# ----------Uid----------------------
    def getUid(self):
        return self.Uid

# ----------username----------------------
    def getUsername(self):
        return self.username

# ----------password--------------------
    def getPassword(self):
        return self.password
