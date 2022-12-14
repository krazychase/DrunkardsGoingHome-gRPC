# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protobuf import tester_pb2 as protobuf_dot_tester__pb2


class TesterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetHello = channel.unary_unary(
                '/tester.Tester/GetHello',
                request_serializer=protobuf_dot_tester__pb2.Message.SerializeToString,
                response_deserializer=protobuf_dot_tester__pb2.Response.FromString,
                )


class TesterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TesterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetHello': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHello,
                    request_deserializer=protobuf_dot_tester__pb2.Message.FromString,
                    response_serializer=protobuf_dot_tester__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tester.Tester', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Tester(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tester.Tester/GetHello',
            protobuf_dot_tester__pb2.Message.SerializeToString,
            protobuf_dot_tester__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)