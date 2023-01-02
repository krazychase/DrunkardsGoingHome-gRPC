'''
Go Home Server
Chase Brown
'''
import grpc
from concurrent import futures
import protobufs.goho_pb2 as pb2
import protobufs.goho_pb2_grpc as pb2_grpc

from user import User
from ride import Ride

class GoHoService(pb2_grpc.GoHoServiceServicer):
    '''
    gRPC Service
    '''
    def __init__(self):
        pass

    def GetUser(self, request, context):
        '''
        Returns User information
        '''
        userID = request.userid
        # Get user info from DB
        user = User()
        response = {'userid':user.userid, 'username':user.username, 'password':user.password, 
                    'home_location':user.homeLocation}

        return pb2.Response(**response)

    def AddUser(self, request, context):
        '''
        Adds user to DB
        Returns confirmation
        '''
        user = User(request.userid, request.username, request.password, request.home_location)
        # Add user to DB
        response = {'response':f'User {user.userid}', 'code':0}

        return pb2.Response(**response)

    def GetRides(self, request, context):
        '''
        Returns ride information
        '''
        rideid = request.rideid
        # Get ride info from DB
        ride = Ride()
        response = {'rideid':ride.rideid, 'rider':ride.rider, 'driver':ride.driver, 
                    'destination':ride.destination, 'location':ride.location, 'time':ride.time, 
                    'status':ride.status}

        return pb2.Response(**response)

    def AddRide(self, request, context):
        '''
        Adds ride to DB
        Returns confirmation
        '''
        ride = Ride(request.rideid, request.rider, request.driver, request.destination, 
                    request.location, request.time, request.status)
        # Add ride to DB
        response = {'response':f'Ride {ride.rideid}', 'code':0}

        return pb2.Response(**response)

    def UpdateRide(self, request, context):
        '''
        Updates ride on DB
        Returns Confirmation
        '''
        ride = Ride(request.rideid, request.rider, request.driver, request.destination, 
                    request.location, request.time, request.status)
        # Update ride in DB
        response = {'response':f'Ride {ride.rideid}', 'code':0}

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GoHoServiceServicer_to_server(GoHoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()