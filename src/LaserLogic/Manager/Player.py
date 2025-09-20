from LaserLogic.Manager.Device import Device
from LaserLogic.Manager.CsvReader.Cards import Cards
from LaserLogic.Manager.CsvReader.Characters import Characters
from LaserLogic.Manager.CsvReader.Skins import Skins

class Players(Device):
    HighID = 0
    LowID = 1
    Token = "None"
    Name = "switlydev"


    SkinsID = Skins.get_skins_id()
    BrawlersID = Characters.get_brawlers_id()
    CardSkillsID = Cards.get_spg_id()
    CardUnlockID = Cards.get_brawler_unlock()
    BrawlerDefaultTrophies = 0
    BrawlersUnlockedState = {}

    BrawlersTrophies = {str(bid): 0 for bid in BrawlersID}
    BrawlersSkins = {str(bid): 0 for bid in BrawlersID}
