import os
import json

class AvailablePackets:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "AvailablePackets.json")
        with open(path, "r") as f:
            self.packet_map = json.load(f)

        if not os.path.exists(path):
            raise FileNotFoundError(f"available_packets.json bulunamadı: {path}")

        with open(path, "r") as f:
            self.packet_map = json.load(f)

    def get_packet_name(self, packet_id):
        return self.packet_map.get(str(packet_id), "UnknownPacket")

    def all(self):
        return self.packet_map
