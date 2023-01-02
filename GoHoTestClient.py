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

    def testAddUser(self):
        '''
        Tests AddUser
        '''

    def testGetRides(self):
        '''
        Tests GetRides
        '''

    def testAddRide(self):
        '''
        Tests AddRides
        '''

    def testUpdateRide(self):
        '''
        Tests UpdateRide
        '''

if __name__ == '__main__':
    client = GoHoClient()
