from LaserLogic.DataStream.Writer import Writer

class OwnHomeData(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.client = client
        self.player = player
    
    def getPacketID(self):
        return 24101
    def readData(self):pass
    def writeData(self):
        pass
        """
        You must find the OwnHomeData structure that suits your client.
        """