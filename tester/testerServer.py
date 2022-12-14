'''
Test server program to see how gRPC works
'''

import grpc
from concurrent import futures
import protobuf.tester_pb2 as pb2
import protobuf.tester_pb2_grpc as pb2_grpc


class TesterService(pb2_grpc.TesterServicer):
    def __init__(self):
        pass

    def GetHello(self, request, context):
        message = request.message
        response = {'message':f"Received '{message}' from client. Hello!", 'code':True}

        return pb2.Response(**response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TesterServicer_to_server(TesterService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()