import random
from src.player import Player

class Game:
    def __init__(self, numbers_of_players):
        self.numbers_of_players = numbers_of_players
        self.players = [Player(f"Player {i}") for i in range(numbers_of_players)]
        self.themes = ["Python", "SQL", "Actualités", "Git", "CLI"]
        self.categories = ["⬛️","🟩","🟪","🟨","🟥","🟦", "🟧"]
        self.perfect_score = [1,2,3,4,5,6]


    def init_grid(self):
        self.grid = Grid(30,30)
        self.init_position = self.grid.init_position()
        return self.grid
    


    def first_player(self):
        pass

    def game_continue(self):
        for num_player in range(self.numbers_of_players):
            if (self.players[num_player].score == self.perfect_score):
                print("Bravo, joueur " + self.players[num_player].name + " gagne la parite !")
                return False
        return True

    def print_players(self):
        for player in self.players:
            print(player.name + " " + player.token)


    def print_score(self):
        for player in self.players:
            affichage = ""
            for score in player.score:
                affichage += self.categories[score]
            print ("le score de " + player.name + " " +affichage)




    

