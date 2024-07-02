import pygame
import socket
import json
import os

pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h))
clock = pygame.time.Clock()

s = socket.socket()

with open("env.json") as f:
    env = json.loads(f.read())

class Connection():
    def __init__(self):
        data = ""
        while True:
            data += s.recv(1024).decode()
            if "§" in data:
                packets = data.split("§")
                data = packets[-1]
                for packet in packets[:-1]:
                    packet = json.loads(packet)
                    getattr(self, packet["type"])

    def tick(self, packet):
        global players
        players = packet["body"]

players = []

s.connect((env["IP"], env["PORT"]))
print(0)
running = True
while running:
    screen.fill((255, 255, 255))

    Connection()
    print(f"{players}\r")

    pygame.display.flip()
    clock.tick(60)