import random
from src.player import Player

class Game:
    def __init__(self, numbers_of_players):
        self.players = [Player(f"Player {i+1}") for i in range(numbers_of_players)]
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

    def game_continue(self):
        for i in range(numbers_of_players):
            if self.players[i].score == 5:
                return False;
        return True;

    def print_players(self):
        for player in self.players:
            print(player.name)

    

