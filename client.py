import socket

class Connection():
    def __init__(self, c: socket.socket):
        self.c = c