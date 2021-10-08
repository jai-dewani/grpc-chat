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

### Setting up the enviroment
- To run the C# server and client, you need to have dotnet 5.x  
Haven't tested it with earlier versions of dotnet, would be a great help if someone could do that 

### Installing Dependencies 

- Install all the C# required packages by going to all three projects base folder `ChatApp`, `ChatAppClient` and `ChatAppServer` to run `dotnet restore`

- Install all the pip packages required for `ChatAppClientPython` by running `pip install -r requirements.txt` 

### Starting up server and client

- First lets start the server, run the following commands to start the server  
    ```
    cd ChatAppServer
    npm start
    ```

- Let's start the C# client. Open a new terminal, make sure you are in the project directory
    ```
    cd ChatAppClient
    npm start
    ```
- Now it's time to start the python client. Open another new terminal, in the same project directory 
    ```
    cd ChatAppClientPython
    python client.py
    ```
- Now both your C# and python client should be able to communicate with each other via the C# server