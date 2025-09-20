from LaserLogic.DataStream.Reader import BSMessageReader
from LaserMessages.Server.Lobby.OwnHomeData import OwnHomeData
from LaserMessages.Server.Auth.AuthOK import AuthOK
from io import BytesIO

class Auth(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def getClient(self):
        return self.client

    def getPlayerData(self):
        return self.player

    def getPacketID(self):
        return 10101

    def readData(self):
        test = self.read_int()

    def writeData(self):
        AuthOK(self.getClient(),self.getPlayerData()).send()
        OwnHomeData(self.getClient(), self.getPlayerData()).send()
