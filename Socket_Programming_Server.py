# Simple Server Using Socket

import socket

HOST ="192.168.1.19"
PORT = 6060
# Step 1 Setting the sever
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

# Step 2 Binding the connection
server.bind((HOST , PORT))

# Step 3 making the server in lestening state
server.listen()

while True :
    # Step 4  Getting Host's communication socket and IP address
    comm_socket , addr = server.accept()
    print(f"Connected to {addr}")
    # Step 5 Receving the message
    msg = comm_socket.recv(1024).decode("utf-8")
    print(f"message from the client is {msg}")
    # Step 6 Sending Infos to the client
    comm_socket.send(f"Got your message Cuh".encode("utf-8"))
    #Terminating the connection
    comm_socket.close()
    print(f"connection with {addr} Ended!")
    
    break

    

    

