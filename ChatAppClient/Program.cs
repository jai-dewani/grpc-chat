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
                    int top = Console.CursorTop;
                    var message = stream.ResponseStream.Current;
                    Console.SetCursorPosition(0,top);
                    Console.WriteLine($"{message.Source}: {message.Message}");
                    Console.Write($"{Name}: ");
                };
                System.Console.WriteLine("DONE");
            });

            while (true)
            {
                Console.Write($"{Name}: ");
                var message = Console.ReadLine();
                int top = Console.CursorTop;
                int left = Console.CursorLeft;
                Console.SetCursorPosition(left,top-1);
                stream.RequestStream.WriteAsync(new Chat { Source = Name, Message = message });
            };
        }
    }
}
