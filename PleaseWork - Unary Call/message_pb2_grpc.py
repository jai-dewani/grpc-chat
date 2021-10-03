# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import message_pb2 as message__pb2


class HelloStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HelloServer = channel.unary_unary(
                '/mess.Hello/HelloServer',
                request_serializer=message__pb2.HelloMessage.SerializeToString,
                response_deserializer=message__pb2.HelloBackMessage.FromString,
                )


class HelloServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HelloServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HelloServer': grpc.unary_unary_rpc_method_handler(
                    servicer.HelloServer,
                    request_deserializer=message__pb2.HelloMessage.FromString,
                    response_serializer=message__pb2.HelloBackMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mess.Hello', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Hello(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HelloServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mess.Hello/HelloServer',
            message__pb2.HelloMessage.SerializeToString,
            message__pb2.HelloBackMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)