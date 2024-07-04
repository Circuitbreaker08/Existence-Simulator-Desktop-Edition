import threading
import pygame
import socket
import json
import os

import connection

pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h))
clock = pygame.time.Clock()

s = socket.socket()

with open("env.json") as f:
    env = json.loads(f.read())

players = []

class Connection(connection.Connection):
    players = players

    def tick(self):
        self.run_queue()

s.connect((env["IP"], env["PORT"]))
c = Connection(s)
running = True
while running:
    screen.fill((255, 255, 255))

    pygame.event.get()

    pygame.display.flip()
    clock.tick(60)