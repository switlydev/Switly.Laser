import time
from threading import Thread
import json
import os
from LaserLogic.Manager.Player import Players
from LaserLogic.Manager.Device import Device
from LaserLogic.Manager.Logger import Logger
#from LaserMessages.PacketHandler import PacketHandler
from LaserMessages.AvailablePackets import AvailablePackets
from LaserMessages.PacketHandler import packet_handlers

class ClientThread(Thread):
    def __init__(self, client, address, server):
        super().__init__(daemon=True)
        self.client = client
        self.address = address
        self.server = server
        self.device = Device(client)
        self.player = Players(self.device)

        self.Logger = Logger()
        self.packet_handlers = packet_handlers

    
    
    def recvall(self, length: int):
        data = b''
        while len(data) < length:
            chunk = self.client.recv(length)
            if not chunk:
                break
            data += chunk
        return data

    def run(self):
        try:
            
            last_packet = time.time()
            while True:
                header = self.client.recv(7)
                if not header:
                    break

                last_packet = time.time()
                packet_id = int.from_bytes(header[:2], 'big')
                length = int.from_bytes(header[2:5], 'big')
                data = self.recvall(length)


                if str(packet_id) in packet_handlers:
                    message_class = packet_handlers[str(packet_id)]
                    message = message_class(self.client, self.player, data)

                    if message.getPacketID() != packet_id:
                        self.Logger.ERROR("The message's packet ID does not match the received packet ID.")
                        
                    else:
                        message.readData()
                        message.writeData()
                        self.Logger.SERVER(f"Packet ID: {packet_id} | From: {self.address[0]}")

                    if packet_id == 10101:
                        self.server.Clients["Clients"][str(self.player.LowID)] = {"SocketInfo": self.client}
                        self.server.Clients["ClientCounts"] = self.server.ThreadCount
                        self.player.ClientDict = self.server.Clients
                else:
                    self.Logger.CLIENT(f"Unknown Packet ID: {packet_id}")

                if time.time() - last_packet > 10:
                    self.Logger.SERVER(f"Connection timeout: {self.address[0]}")
                    self.client.close()
                    break

        except (ConnectionAbortedError, ConnectionResetError, TimeoutError):
            print(f"Connection lost: {self.address[0]}")
            self.client.close()
    
    def __del__ (self):
        try:
            print(f"[X] {self.address[0]} bağlantısı temizleniyor...")
            """self.client.close()
            del self.player
            del self.device"""
        except Exception as e:
            self.Logger.ERROR("Error:",e)
        finally: pass
        """ self.client.close()
            del self.player
            del self.device"""
