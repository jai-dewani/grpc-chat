import random
import logging
import asyncio 

import grpc

import chat_app_pb2_grpc
import chat_app_pb2


# def ReadChatMessages(stub):


# def SendChatMessages(stub):
#     responses = stub.ChatStream
def TakeInput(name):
    while True:
        text = input()
        message = chat_app_pb2.Chat(source=name, message=text)
        yield message

def chat(stub, name):
    responses = stub.ChatStream(TakeInput(name))

    for response in responses:
        print(response.source + ": " + response.message)

def run():
    with grpc.insecure_channel("localhost:55005") as channel: 
        name = input("What's your name?: ")
        stub = chat_app_pb2_grpc.ChatServiceStub(channel)
        # stub.ChatStream()
        # stub.ChatStream
        # loop = asyncio.get_event_loop()
        # tasks = [
        #     loop.create_task(SendChatMessages(stub)),
        #     loop.create_task(ReadChatMessages(stub))
        # ]
        # loop.run_until_complete(asyncio.wait(tasks))
        # loop.close()
        chat(stub,name)

if __name__ == '__main__':
    run()