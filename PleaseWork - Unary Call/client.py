import grpc 

import message_pb2
import message_pb2_grpc
  

def run():
    channel = grpc.insecure_channel('localhost:505050')
    stub = message_pb2_grpc.HelloStub(channel)
    Name = input("Name: ")
    Message = input("Message: ")

    helloMessage = message_pb2.HelloMessage(name = Name, message = Message)
    print(helloMessage.name)
    response = stub.HelloServer(helloMessage)
    print(response.name + ": " + response.message)

run()