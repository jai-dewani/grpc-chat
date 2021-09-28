using System;
using ChatApp;
using Grpc.Core; 

namespace ChatAppServer
{
    class Program
    {
        static void Main(string[] args)
        {
            const int Port = 55005;
            
            Server server = new Server
            {
                Services = { ChatService.BindService(new ChatAppProxy()) },
                Ports = { new ServerPort("localhost",Port,ServerCredentials.Insecure)}
            };
            server.Start();
            System.Console.WriteLine($"Server Started on Port {Port}");
            System.Console.WriteLine("Press any key to stop the server");
            Console.ReadKey();

            server.ShutdownAsync().Wait();
        }
    }
}
