'''
Go Home Server
Chase Brown
'''
import grpc
from concurrent import futures
import protobufs.goho_pb2 as pb2
import protobufs.goho_pb2_grpc as pb2_grpc

class User():
    def __init__(self):
        pass

class Ride():
    def __init__(self):
        pass

class GoHoService():
    def __init__(self):
        pass

    def GetUser():
        pass

    def AddUser():
        pass

    def GetRides():
        pass

    def AddRide():
        pass

    def UpdateRide():
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GoHoServiceServicer_to_server(GoHoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()