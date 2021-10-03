import message_pb2
import message_pb2_grpc

from concurrent import futures
import grpc 

class MessageServicer(message_pb2_grpc.HelloServicer):

    def __init__(self):
        self.message = None 

    def HelloServer(self, request, context):
        print("aba daba jabba")
        print(request.name + ": " + request.message)
        response = message_pb2.HelloBackMessage(name="Jai",message="Working!!")
        return response

def Server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_HelloServicer_to_server(
        MessageServicer(), server
    )
    server.add_insecure_port('[::]:505050')
    server.start()
    print("Server started")
    server.wait_for_termination()

Server()