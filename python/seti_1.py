#!/usr/bin/env python3
import socket
#initializing socket
s = socket.socket()
host = socket.gethostname()
port = 12345

# connect to host
s.connect((host,port))

print(s.recv(1024).decode())
s.close()
