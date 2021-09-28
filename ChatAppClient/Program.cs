using System;
using Grpc.Core;
using ChatApp;
using System.Threading.Tasks;

namespace ChatAppClient
{
    class Program
    {
        static void Main(string[] args)
        {
            const int Port = 55005;
            var channel = new Channel("localhost", Port, ChannelCredentials.Insecure);
            var client = new ChatService.ChatServiceClient(channel);

            AsyncDuplexStreamingCall<Chat,Chat> stream = client.ChatStream();
            Console.Write("What's your name?: ");
            string Name = Console.ReadLine();

            var readResponses = Task.Run(async () =>
            {
                while (await stream.ResponseStream.MoveNext())
                {
                    System.Console.WriteLine("MESSAGE");
                    var message = stream.ResponseStream.Current;
                    Console.WriteLine($"{message.From}: {message.Message}");
                };
                System.Console.WriteLine("DONE");
            });

            while (true)
            {
                var message = Console.ReadLine();
                stream.RequestStream.WriteAsync(new Chat { From = Name, Message = message });
            };
        }
    }
}
