using ChatApp;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

using Grpc.Core;

namespace ChatAppServer
{
    class ChatAppProxy : ChatService.ChatServiceBase
    {
        private IList<IServerStreamWriter<Chat>> clients;

        public ChatAppProxy()
        {
            clients = new List<IServerStreamWriter<Chat>>();
        }

        public override async Task ChatStream(IAsyncStreamReader<Chat> requestStream, IServerStreamWriter<Chat> responseStream, ServerCallContext content)
        {
            clients.Add(responseStream);
            Console.WriteLine("New Listener");
            while(await requestStream.MoveNext())
            {
                var message = requestStream.Current;
                Console.WriteLine(message.Message);
                this.SendMessage(message);
            }
            Console.WriteLine("END");
            clients.Remove(responseStream);
        }

        private void SendMessage(Chat message)
        {
            foreach(var client in this.clients)
            {
                client.WriteAsync(message);
            }
        }

    }
}