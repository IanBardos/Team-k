class Notification:
    """
    this is Notification class for Course

    it contains elements of a Notification

    Contain parameter:
        Nid -- int -- id to identify the Notification (must be unique) -- static
        subscription--  int -- Sid(from class Subscription) -- static -- subscription id

    Contain function:
        Notification(Nid, user)
            --- constructor
        --- acessor methods for attributes
        getNid(self)
        getUser(self)
    """

    def __init__(self, Nid, subscription):
        # Nid -- int
        # subscription -- int -- Uid
        self.Nid = Nid
        self.subscription = subscription

    def getNid(self):
        return self.Nid

    def getSubcription(self):
        return self.subscription
