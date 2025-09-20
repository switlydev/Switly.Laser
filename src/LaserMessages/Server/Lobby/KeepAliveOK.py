from LaserLogic.DataStream.Writer import Writer 



class KeepAliveOK(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.client = client
        self.player = player
    def getPacketID(self):
        return 20108
    
    def readData(self):pass
    def writeData(self):
        self.writeVint(0)
