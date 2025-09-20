import socket
import os
import pyfiglet
import json
from LaserLogic.Network.Client import ClientThread
from LaserLogic.Manager.Logger import Logger


class Server:
    Clients = {"ClientCounts": 0, "Clients": {}}
    ThreadCount = 0

    def __init__(self, ip: str, port: int):
        self.server = socket.socket()
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.port = port
        self.ip = ip

    def start(self):
        log = Logger()
        self.server.bind((self.ip, self.port))
        with open("config.json", "r") as f:
            data = json.load(f)
        coolstuf = pyfiglet.figlet_format(data["ServerName"],font="slant")
        print(coolstuf)
        log.SERVER(f"Server started at {self.ip}:{self.port}")

        while True:
            self.server.listen()
            client, address = self.server.accept()
            log.SERVER(f"New connection from {address[0]}")
            ClientThread(client, address, self).start()
            Server.ThreadCount += 1
