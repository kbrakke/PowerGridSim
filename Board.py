import ResourceTrack, PowerPlantMarket

 class board():
     def __init__(self, side, number_players):
        self.side = side
        self.number_players = number_players
        self.player_order = []
        self.resources = ResourceTrack(self.side)
        self.market = PowerPlantMarket(self.side, self.number_players)
        self.grid = PowerGrid(self.side, self.number_players)


