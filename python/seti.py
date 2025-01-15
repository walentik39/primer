#!/usr/bin/env python3
import socket
import datetime
#initializing socket
s = socket.socket()
host = socket.gethostname()
port = 12345

#binding port and host
s.bind((host,port))

# waiting for a client to connect
s.listen(5)

while True:
    c, addr = s.accept()
    print('get connection from addr', addr)
    date = datetime.datetime.now()
    d = str(date)
    c.send(d.encode())
    c.close()
