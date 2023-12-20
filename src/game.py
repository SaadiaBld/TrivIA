import random
from src.player import Player
from src.board import Board

class Game:
    def __init__(self, numbers_of_players, boardgame):
        self.numbers_of_players = numbers_of_players
        self.players = [Player(i, boardgame) for i in range(numbers_of_players)]
        self.categories = ["⬛️","🟩","🟪","🟨","🟥","🟦", "🟧"]
        self.perfect_score = [1,2,3,4,5,6]
        self.actual_player = 0


    def next_player(self):
        self.actual_player += 1
        self.actual_player = self.actual_player % self.numbers_of_players


    def game_continue(self):
        for num_player in range(self.numbers_of_players):
            if (self.players[num_player].score == self.perfect_score):
                print("Bravo, " + self.players[num_player].token  + " gagne la parite !")
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
            print ("le score de " + player.token + " " + affichage)


    def roll_dice():
        # tirer au sort un nombre entre 1 et 6
        dice_number = random.choice(range(1,7))
        return dice_number
        # dé 3D? comment animer un .obj en python?
        # dé 3D? animations Blender
        # images des faces d'un dé?




    

