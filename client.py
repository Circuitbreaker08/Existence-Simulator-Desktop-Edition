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

    def __main_error__(self):
        pass

    def game_state(self):
        pass

s.connect((env["IP"], env["PORT"]))
c = Connection(s)
running = True
while running:
    c.run_queue()

    screen.fill((255, 255, 255))

    pygame.event.get()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()