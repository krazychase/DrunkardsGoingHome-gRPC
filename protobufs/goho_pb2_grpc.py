# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protobufs import goho_pb2 as protobufs_dot_goho__pb2


class GoHoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUser = channel.unary_unary(
                '/goho.GoHoService/GetUser',
                request_serializer=protobufs_dot_goho__pb2.GetUserRequest.SerializeToString,
                response_deserializer=protobufs_dot_goho__pb2.User.FromString,
                )
        self.AddUser = channel.unary_unary(
                '/goho.GoHoService/AddUser',
                request_serializer=protobufs_dot_goho__pb2.User.SerializeToString,
                response_deserializer=protobufs_dot_goho__pb2.Confirmation.FromString,
                )
        self.GetRides = channel.unary_stream(
                '/goho.GoHoService/GetRides',
                request_serializer=protobufs_dot_goho__pb2.GetRideRequest.SerializeToString,
                response_deserializer=protobufs_dot_goho__pb2.Ride.FromString,
                )
        self.AddRide = channel.unary_unary(
                '/goho.GoHoService/AddRide',
                request_serializer=protobufs_dot_goho__pb2.Ride.SerializeToString,
                response_deserializer=protobufs_dot_goho__pb2.Confirmation.FromString,
                )
        self.UpdateRide = channel.unary_unary(
                '/goho.GoHoService/UpdateRide',
                request_serializer=protobufs_dot_goho__pb2.Ride.SerializeToString,
                response_deserializer=protobufs_dot_goho__pb2.Confirmation.FromString,
                )


class GoHoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRides(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddRide(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRide(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GoHoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=protobufs_dot_goho__pb2.GetUserRequest.FromString,
                    response_serializer=protobufs_dot_goho__pb2.User.SerializeToString,
            ),
            'AddUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUser,
                    request_deserializer=protobufs_dot_goho__pb2.User.FromString,
                    response_serializer=protobufs_dot_goho__pb2.Confirmation.SerializeToString,
            ),
            'GetRides': grpc.unary_stream_rpc_method_handler(
                    servicer.GetRides,
                    request_deserializer=protobufs_dot_goho__pb2.GetRideRequest.FromString,
                    response_serializer=protobufs_dot_goho__pb2.Ride.SerializeToString,
            ),
            'AddRide': grpc.unary_unary_rpc_method_handler(
                    servicer.AddRide,
                    request_deserializer=protobufs_dot_goho__pb2.Ride.FromString,
                    response_serializer=protobufs_dot_goho__pb2.Confirmation.SerializeToString,
            ),
            'UpdateRide': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRide,
                    request_deserializer=protobufs_dot_goho__pb2.Ride.FromString,
                    response_serializer=protobufs_dot_goho__pb2.Confirmation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'goho.GoHoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GoHoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/goho.GoHoService/GetUser',
            protobufs_dot_goho__pb2.GetUserRequest.SerializeToString,
            protobufs_dot_goho__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/goho.GoHoService/AddUser',
            protobufs_dot_goho__pb2.User.SerializeToString,
            protobufs_dot_goho__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRides(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/goho.GoHoService/GetRides',
            protobufs_dot_goho__pb2.GetRideRequest.SerializeToString,
            protobufs_dot_goho__pb2.Ride.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddRide(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/goho.GoHoService/AddRide',
            protobufs_dot_goho__pb2.Ride.SerializeToString,
            protobufs_dot_goho__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRide(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/goho.GoHoService/UpdateRide',
            protobufs_dot_goho__pb2.Ride.SerializeToString,
            protobufs_dot_goho__pb2.Confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
