import socket
import os

s = socket.socket()


class Connection():
    def __init__(self, c: socket.socket):
        self.c = c


s.connect((os.environ["IP"], int(os.environ["PORT"])))