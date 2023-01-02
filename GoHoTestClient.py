'''
Go Home Testing Client
Chase Brown
'''
import grpc
import protobufs.goho_pb2 as pb2
import protobufs.goho_pb2_grpc as pb2_grpc

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
        message = pb2.GetUserRequest(userid=12345)
        response = self.stub.GetUser(message)
        print(response)

    def testAddUser(self):
        '''
        Tests AddUser
        '''
        user = User()
        message = pb2.User(userid=12345, username=user.username, password=user.password, home_location=user.homeLocation)
        response = self.stub.AddUser(message)
        print(response)

    def testGetRides(self):
        '''
        Tests GetRides
        '''
        message = pb2.GetRideRequest(rideid=12345)
        response = self.stub.GetRides(message)
        for resp in response:
            print(resp)

    def testAddRide(self):
        '''
        Tests AddRides
        '''
        ride = Ride()
        message = pb2.Ride(rideid=98765, rider=ride.rideid, driver=ride.driver, destination=ride.destination, location=ride.location, time=ride.time, status=ride.status)
        response = self.stub.AddRide(message)
        print(response)
        

    def testUpdateRide(self):
        '''
        Tests UpdateRide
        '''
        ride = Ride()
        message = pb2.Ride(rideid=98765, rider=ride.rideid, driver=ride.driver, destination=ride.destination, location=ride.location, time=ride.time, status=ride.status)
        response = self.stub.UpdateRide(message)
        print(response)

if __name__ == '__main__':
    client = GoHoClient()
    print('Beginning Tests . . . ')
    print('Testing Get User . . . ')
    client.testGetUser()
    print('Testing Add User . . . ')
    client.testAddUser()
    print('Testing Get Rides . . . ')
    client.testGetRides()
    print('Testing Add Ride . . . ')
    client.testAddRide()
    print('Testing Update Ride . . . ')
    client.testUpdateRide()
    print('Testing Complete.')
