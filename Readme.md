# CLI Chat application using gRPC 

This project was created for a talk I did at [APIHacks](http://apihacks.co/) about how to get started with gRPC and why/when you should choose it over REST. You can watch the talk here [What's gRPC? and Why gRPC over REST? | Jai Dewani at API Hacks](https://youtu.be/rMdlCBYbY7Q). 

## Why? 

The main movtive of this project is to showcase the bidirectional streaming capablity of gRPC as well as the capability of connecting a client and a server which are using two completly different language. 

## Project Directory 

Now I will try to make some sense out of this project directory 

- **PleaseWork - Unary Call**: A very simple one gRPC method implimentation in python, you can find all the required files and instructions inside the folder on what each file does and how to get the project up and running 

- **ChatApp**: This is a Dotnet Library I created which is responsible for compiling the proto file, so by referencing this project in the Server and Client we can directly work with compiled gRPC interfaces in C#. All I did was include the correct PackageReference's and adding the path to the proto file in the csproj file. 

- **ChatAppClient**: A dotnet CLI project. It connects to the `ChatAppServer` to send and receive messages in a bi-drectional stream. 

- **ChatAppServer**: A dotnet CLI project that impliments the server interface that `ChatApp` genrates. 

- **ChatAppClientPython**: A python script that uses the python stub genrated from the protobuf to make RPC calls to `ChatAppServer` project.  


## How to ChatApp setup project

TODO
