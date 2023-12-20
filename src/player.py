from random import *
from board import *

class Player:

    def __init__(self, board):
        tokens = ["🦊","🐨","🐼","🐸","🐱"]
        #self.id = int(player_id)
        self.name = input(f"Player{self.id +1}, what's your name?: ")
        self.token = "🦊"
        self.score = [0,0,0,0,0,0]
        self.x = 6
        self.y = 6
        self.new_x = 0
        self.new_y = 0
        self.board = board
        #player_id enlevé ici de init
    
    #def roll_dice(self):
    #    dice = randint(1, 6)
    #    return dice
    
    def choose_move(self):
        """On définit ici la logique de déplacement lorsque le joueur est dans les arêtes du milieu"""
        """if self.y == 6 and self.x == 6:
            choix1 = self.x + self.roll_dice()
            choix2 = self.x - self.roll_dice()
            choix3 = self.y + self.roll_dice()
            choix4 = self.y - self.roll_dice()

            print("Choisissez votre déplacement: ")
            print(f" 1. Vers la droite : {choix1}")
            print(f" 2. Vers la gauche : {choix2}")
            print(f" 3. Vers le haut: {choix4}")
            print(f" 4. Vers le bas : {choix3}")

            direction_choix = input("Choisissez votre direction:  ")
            if direction_choix == "1":
                self.x = choix1
            elif direction_choix == "2":
                self.x = choix2
            elif direction_choix == "3":
                self.y = choix3
            elif direction_choix == "4":
                self.y = choix4

            return self.y,self.x                
        
        if self.y == 6: #si le joueur est sur la ligne indice 6
            choix1 = self.x + self.roll_dice()
            choix2 = self.x - self.roll_dice()
            position_choix = input("Choisissez votre déplacement: {} or {}".format(choix1,choix2 ))
            self.x = int(position_choix)
            return self.y,self.x
        
        if self.x == 6:
            choix1 = self.y + self.roll_dice()
            choix2 = self.y - self.roll_dice()
            position_choix = input("Choisissez votre déplacement: {} ou  {}".format(choix1,choix2))
            self.y = int(position_choix)
            return self.y, self.x"""
        
        """for i in range (5):
            self.x +=1
        self.new_x =self.x
        self.new_y = self.y
        self.update_position()
        return self.x, self.y"""
        

    def answer_question(self):
        return self.board.ask_question() 
        

    def update_position(self):
        old_value = self.board.grid[self.y][self.x]
        if self.answer_question():
            self.board.grid[self.y][self.x]=old_value
            self.board.grid[self.new_y][self.new_x] = self.token
    
    def upgrade_score(self):
        if self.answer_question():
            self.score += 1
        return self.score
    
    def show_score(self):
        return self.score