import socket
import time
import sys

texts = []

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        texts.append(arg)
else:
    texts.append("Default Text")

for text in texts:
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('zero', 8089))
    clientsocket.send(text.encode('UTF-8'))
    clientsocket.close()
    time.sleep(0.5)