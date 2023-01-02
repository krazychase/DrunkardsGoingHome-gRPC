class User():
    '''
    Contains User information
    '''
    def __init__(self, userid=None, username=None, password=None, homeLocation=None):
        self.userid = userid
        self.username = username
        self.password = password
        self.homeLocation = homeLocation