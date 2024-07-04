import threading
import socket
import json

class Connection():
    players = []

    def __init__(self, c: socket.socket):
        self.c = c
        self.func_queue = {}
        Connection.players.append(self)
        threading.Thread(target=self.main, daemon=True).start()

    def main(self):
        data = ""
        try:
            while True:
                data += self.c.recv(1024).decode()
                if "§" in data:
                    data = data.split("§", 1)
                    packet = json.loads(data[0])
                    data = data[1]
                    getattr(self, packet["type"])(packet)
                
        except ConnectionResetError:
            Connection.players.remove(self)

    def run_queue(self):
        pass