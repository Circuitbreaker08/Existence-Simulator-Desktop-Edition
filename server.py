from __future__ import annotations

import threading
import socket
import json
import os

import connection

from pygame import time

with open("env.json") as f:
    env = json.loads(f.read())

s = socket.socket()
clock = time.Clock()
players: list[Connection] = []

def connection_accept():
    print("listening")
    while True:
        c, addr = s.accept()
        print(f"Accepted connection from {addr}")
        Connection(c)

class Connection(connection.Connection):
    players = players

    def tick(self):
        self.run_queue()

s.bind(('', env["PORT"]))

s.listen()

threading.Thread(target=connection_accept, daemon=True).start()

print(f"Server opened on port {env["PORT"]}")

while True:
    clock.tick(60)