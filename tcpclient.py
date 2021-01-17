#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

clientsocket.connect(('sender ip', port))

message = clientsocket.recv(2048)

clientsocket.close()

print(message.decode('ascii'))