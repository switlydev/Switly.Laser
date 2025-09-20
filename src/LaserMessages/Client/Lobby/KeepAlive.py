
from LaserLogic.DataStream.Reader import BSMessageReader
from LaserMessages.Server.Lobby.KeepAliveOK import KeepAliveOK

class KeepAlive(BSMessageReader):
    def __init__(self, client,player,initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player
    
    def getPacketID(self):
        return 10108
    
    def getClient(self):
        return self.client
    def getPlayerData(self):
        return self.player
    def readData(self):pass
    def writeData(self):
        KeepAliveOK(self.getClient(),self.getPlayerData()).send()