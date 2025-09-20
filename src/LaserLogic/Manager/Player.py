from LaserLogic.Manager.Device import Device
from LaserLogic.Manager.CsvReader.Cards import Cards
from LaserLogic.Manager.CsvReader.Characters import Characters
from LaserLogic.Manager.CsvReader.Skins import Skins

class Players(Device):
    HighID = 0
    LowID = 1
    Token = "None"
    Name = "switlydev"
    Trophies = 0
    HighestTrophies = 0
    TrophyRoadClaimed = 100
    ProfileIcon = 0
    NameColor = 0
    TokenDoubler = 200
    BattleTokens = 200
    Tickets = 0
    BrawlerID = 0
    BrawlBoxes = 1000
    BigBoxes = 100
    StarPoints = 1000
    Gold = 1000
    ThemeID = 1
    Gems = 99999
    Tutorial = 2
    Region = "TR"
    SupportedContentCreator = "switlydev"
    BrawlerDefaultTrophies = 0
    UnlockedSkins = []

    SkinsID = Skins.get_skins_id()
    BrawlersID = Characters.get_brawlers_id()
    CardSkillsID = Cards.get_spg_id()
    CardUnlockID = Cards.get_brawler_unlock()
    BrawlerDefaultTrophies = 0
    BrawlersUnlockedState = {}
    # Hatalı olan: for döngüsü class içinde olamaz
    # Çözüm: dict comprehension direkt class içinde yazılır
    BrawlersTrophies = {str(bid): 0 for bid in BrawlersID}
    BrawlersSkins = {str(bid): 0 for bid in BrawlersID}
