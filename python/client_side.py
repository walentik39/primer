#!/usr/bin/env python3

import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 22

# connect to the server on local computer
s.connect(('8.8.8.8', port))

# receive data from the server and decoding to get the string.
print(s.recv(1024).decode())
# close the connection
s.close()
