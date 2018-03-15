class Comment:
    """
    this is comment class for the Topic

    it contains elements of a comment

    Contains parameter:
        commenter -- User(User.py) -- static
        info -- string
        addon -- string
        
    Contain function:
        Comment(commenter, info, addon)
            ---constractor
        setInfo(info)
        getInfo()
        setAddon(addon)
        setAddon()

    --- info is comment

    --- addon is a address(in database) of a file or a link that user posted
    
    """
    def __init__(self, commenter, info, addon):
        ## commenter -- User(User.py)
        ## info -- string
        ## addon -- string
        self.commenter = commenter
        self.info = info
        self.addon = addon

    def setInfo(self,info):
        ## info -- string
        self.info = info

    def getInfo(self):
        return self.info


    def setAddon(self,addon):
        ## addon -- string
        self.addon = addon

    def getAddon(self):
        return self.addon
    
