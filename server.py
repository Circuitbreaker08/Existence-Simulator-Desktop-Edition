import threading
import socket
import json
import os

from pygame import time

s = socket.socket()
clock = time.Clock()

class Connection():
    def __init__(self, c: socket.socket):
        self.c = c
        self.position = [0, 0]
        players.append(self)

    def tick(self):
        data = ""
        player_input = None
        while True:
            data += self.c.recv(1024).decode()
            if "§" in data:
                packets = data.split("§")
                data = packets[-1]
                for packet in packets[:-1]:
                    packet = json.loads(packet)
                    if packet["type"] == "input":
                        player_input = packet
            else:
                break
        if player_input != None:
            self.position[0] += player_input["body"][0]
            self.position[1] += player_input["body"][1]

    def transmit(self):
        return {"position": self.position}

def connection_accept():
    while True:
        c, addr = s.accept()
        Connection(c)


players: list[Connection] = []

s.bind(('', int(os.environ["PORT"])))

s.listen()

threading.Thread(target=connection_accept, daemon=True)

print(f"Server opened on port {os.environ["PORT"]}")

while True:
    for player in players:
        player.tick()

    for player in players:
        player.c.send(json.dumps({"type": "tick", "body": [x.transmit() for x in players]}).encode())

    clock.tick(60)