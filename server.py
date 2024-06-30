import threading
import socket

s = socket.socket()

class Connection():
    def __init__(self, c: socket.socket):
        self.c = c
        players.append(self)

    def tick():
        pass

def connection_accept():
    c, addr = s.accept()
    Connection(c)

players: list[Connection] = []

s.bind(('', 8765))

s.listen()

threading.Thread(target=connection_accept)