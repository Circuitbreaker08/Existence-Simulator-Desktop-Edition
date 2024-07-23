from __future__ import annotations

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
    queue_funcs = ["game_state"]

    def game_state(self, payload):
        global players
        players = payload["body"]

    def __main_error__(self):
        pass

s.connect((env["IP"], env["PORT"]))
c = Connection(s)
running = True
while running:
    c.run_queue()

    screen.fill((255, 255, 255))

    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    s.send(f"{json.dumps({"type": "input", "body": [keys[pygame.K_d] - keys[pygame.K_a], keys[pygame.K_s] - keys[pygame.K_w]]})}§".encode())

    for player in players:
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(player, (32, 32)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()