# Simple Client using socket

import socket

HOST="192.168.1.19"
PORT=6060

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect((HOST , PORT))

client.send("hello I am the client".encode("utf-8"))

msg = client.recv(1024).decode("utf-8")

print(msg)
