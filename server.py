from __future__ import annotations

import threading
import socket
import json
import os

from pygame import time

import connection

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
    queue_funcs = []

    def __init__(self, c):
        self.players.append(self)
        super().__init__(c)

    def __main_error__(self):
        self.players.remove(self)

s.bind(('', env["PORT"]))

s.listen()

threading.Thread(target=connection_accept, daemon=True).start()

print(f"Server opened on port {env["PORT"]}")

while True:
    for conn in players:
        conn.run_queue()
    clock.tick(60)