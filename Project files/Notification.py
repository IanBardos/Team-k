class Notification:
    """
    this is Notification class for Course

    it contains elements of a Notification

    Contain parameter:
        Nid -- int -- id to identify the Notification (must be unique) -- static
        subcription --  int -- Sid(from class Subscription) -- static -- subcription id

    Contain function:
        Notification(Nid, user)
            --- constructor
        --- acessor methods for attributes
        getNid(self)
        getUser(self)
    """

    def __init__(self, Nid, subcription):
        # Nid -- int
        # subscription -- int -- Uid
        self.Nid = Nid
        self.subscription = subcription

    def getNid(self):
        return self.Nid

    def getSubcription(self):
        return self.subscription
