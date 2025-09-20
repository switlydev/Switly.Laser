from LaserLogic.DataStream.Writer import Writer 
import json


class AuthOK(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.client = client
        self.player = player
    def getPacketID(self):
        return 20104
    
    def readData(self):pass

    def writeData(self):
        json_data = json.load(open("config.json"))

        # Account ID
        self.writeInt(self.player.HighID)
        self.writeInt(self.player.LowID)

        # Home ID
        self.writeInt(self.player.HighID)
        self.writeInt(self.player.LowID)

        self.writeString(self.player.Token)  # Pass Token       
        self.writeString() # Facebook ID
        self.writeString() # Gamecenter ID

        self.writeInt(json_data["ClientMajor"])   # Major Version
        self.writeInt(json_data["ClientMinor"])  # Minor Version
        self.writeInt(json_data["ClientBuild"])    # Build Version

        self.writeString("dev")  # Environment

        self.writeInt(0)  # Session Count
        self.writeInt(0)  # Play Time Seconds
        self.writeInt(0) # Days Since Started Playing

        self.writeString()  
        self.writeString() 
        self.writeString()

        self.writeInt(0)

        self.writeString()

        self.writeString("TR") # Region
        self.writeString()

        self.writeInt(1)

        self.writeString()  
        self.writeString() 
        self.writeString()

        self.writeVint(0)

        self.writeString()

        self.writeVint(1)


