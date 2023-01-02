class Ride():
    '''
    Contains Ride Information
    '''
    def __init__(self, rideid=None, rider=None, driver=None, destination=None, location=None, 
                time=None, status=None):
        self.rideid = rideid
        self.rider = rider
        self.driver = driver
        self.destination = destination
        self.location = location
        self.time = time
        self.status = status
