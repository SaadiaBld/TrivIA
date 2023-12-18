import random
    

class Game:
    def __init__(self, numbers_of_players=1):
        self.numbers_of_players = numbers_of_players
        self.players = []
        self.themes = ["Python", "SQL", "Actualités", "Git", "CLI"]

    def init_grid(self):
        self.grid = Grid(30,30)
        self.init_position = self.grid.init_position()
        return self.grid
    
    def init_players(self, names, colors):
        for name, color in names, colors:
            self.players.append(Player(name, color, self.init_position))
        return self.players

    def first_player(self):
        pass






