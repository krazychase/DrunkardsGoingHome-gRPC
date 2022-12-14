'''
Test client program to see how gRPC works
'''

import grpc
import protobuf.tester_pb2_grpc as pb2_grpc
import protobuf.tester_pb2 as pb2


class TesterClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.TesterStub(self.channel)

    def GetMessage(self, message):
        message = pb2.Message(message=message)
        return self.stub.GetHello(message)


if __name__ == '__main__':
    client = TesterClient()
    result = client.GetMessage(message="Hello Server!")
    print(f'{result}')