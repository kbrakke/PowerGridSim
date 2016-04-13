class PowerPlantMarket():
    def __init__(self, side, number_players):
        self.side = side
        self.number_players = number_players
        self.deck = self.initDeck(self.side, self.number_players)
        self.currentMarket = []
        self.futuresMarket = []

    def initDeck(self, side, number_players):
        pass
    def cleanupMarket(self, stage):
        pass
