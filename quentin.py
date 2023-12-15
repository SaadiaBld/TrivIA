import random
    

class Game:
    def __init__(self, numbers_of_players=1):
        self.numbers_of_players = numbers_of_players
        self.players = []
        self.themes = ["Python", "SQL", "Actualités", "Git", "CLI"]

    def init_grid(self):
        self.grid = Grid()
    
    def init_players(self, names):
        for name in names:
            self.players.append(Player(name))
        return self.players

    def first_player(self):
        pass



class Grid:
    def __init__(self, themes):
        self.width = 10
        self.height = 10
        self.themes = themes
        self.cases = []

    def create_cases(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append({"position": (i,j), "active": True, "theme": random.sample})
            self.cases.append(row)

