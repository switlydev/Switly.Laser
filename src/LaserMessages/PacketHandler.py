# src/LaserMessages/packet_handlers.py

from LaserMessages.Client.Auth.Auth import Auth
from LaserMessages.Client.Lobby.KeepAlive import KeepAlive
from LaserMessages.Server.Auth.AuthOK import AuthOK
from LaserMessages.Server.Lobby.OwnHomeData import OwnHomeData
from LaserMessages.Server.Lobby.KeepAliveOK import KeepAliveOK
packet_handlers = {
    "10101": Auth,
    "10108": KeepAlive,
    "20104":AuthOK,
    "20108":KeepAliveOK,
    "24101": OwnHomeData
}
