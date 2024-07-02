import socket
import json
import os

s = socket.socket()

with open("env.json") as f:
    env = json.loads(f.read())

class Connection():
    def __init__(self, c: socket.socket):
        self.c = c


s.connect((env["IP"], env["PORT"]))