'''
Go Home Testing Client
Chase Brown
'''
import grpc
import protobufs.goho_pb2 as pb2
import protobufs.goho_pb2_grpc as pb2_grpc
from datetime import datetime, timezone

from user import User
from ride import Ride

class GoHoClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.GoHoServiceStub(self.channel)

    def testGetUser(self):
        '''
        Tests GetUser
        '''
        message = pb2.GetUserRequest(userid=1)
        response = self.stub.GetUser(message)
        print(response)

    def testAddUser(self):
        '''
        Tests AddUser
        '''
        user = User(None, 'TestName', 'TestPass', 'TestLocation')
        message = pb2.User(userid=user.userid, username=user.username, password=user.password, home_location=user.homeLocation)
        response = self.stub.AddUser(message)
        print(response)

    def testGetRides(self):
        '''
        Tests GetRides
        '''
        message = pb2.GetRideRequest(rideid=1)
        response = self.stub.GetRides(message)
        for resp in response:
            print(resp)

    def testAddRide(self):
        '''
        Tests AddRides
        '''
        ride = Ride(None, 1, 1, 'TestDestination', 
            'TestLocation', str(datetime.now(timezone.utc)), 'ACTIVE')
        message = pb2.Ride(rideid=ride.rideid, rider=ride.rider, driver=ride.driver, destination=ride.destination, 
                            location=ride.location, time=ride.time, status=ride.status)
        response = self.stub.AddRide(message)
        print(response)

    def testUpdateRide(self):
        '''
        Tests UpdateRide
        '''
        ride = Ride(rideid=1, status='COMPLETE')
        message = pb2.Ride(rideid=ride.rideid, rider=ride.rider, driver=ride.driver, destination=ride.destination, 
                            location=ride.location, time=ride.time, status=ride.status)
        response = self.stub.UpdateRide(message)
        print(response)

if __name__ == '__main__':
    client = GoHoClient()
    print('Beginning Tests . . . ')
    print('Testing Add User . . . ')
    client.testAddUser()
    print('Testing Get User . . . ')
    client.testGetUser()
    print('Testing Add Ride . . . ')
    client.testAddRide()
    print('Testing Get Rides . . . ')
    client.testGetRides()
    print('Testing Update Ride . . . ')
    client.testUpdateRide()
    client.testGetRides()
    print('Testing Complete.')
