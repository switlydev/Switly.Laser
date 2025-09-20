from LaserLogic.Network.Server import Server
import json
json_data = json.load(open("config.json"))
server = Server(json_data["ServerIP"], json_data["ServerPort"])
server.start()