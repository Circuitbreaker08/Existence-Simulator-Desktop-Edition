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
players: list[Player] = []

def connection_accept():
    print("listening")
    while True:
        c, addr = s.accept()
        print(f"Accepted connection from {addr}")
        Player(c)

class Player(connection.Connection):
    players = players
    queue_funcs = ["input"]

    def input(self, payload):
        self.position[0] += payload["body"][0]
        self.position[1] += payload["body"][1]

    def __init__(self, c):
        self.position = [0, 0]

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

    global_update = json.dumps({"type": "game_state", "body": [x.position for x in players]})

    for conn in players:
        conn.c.send(f"{global_update}§".encode())

    clock.tick(60)