import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('zero', 8089))
clientsocket.send('hello'.encode('UTF-8'))