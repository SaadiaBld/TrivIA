import random
#from board import *
# from src.game import *
#attention, ici tests sont inclus ainsi que les modifs liées aux fonctions deplacées depuis board

# Add jeremy
import json
import networkx as nx


class Player:
    def __init__(self, id, board):
        tokens = ["🦊","🐨","🐼","🐸","🐱"]
        self.name = input(f"What's your name?: ")
        self.token = tokens[id]
        self.score = [0,0,0,0,0,0]#["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"]
        self.perfect_score = ["🟩","🟪","🟨","🟥","🟦", "🟧"]
        self.x = board.col
        self.y = board.row_middle
        self.new_x = 6
        self.new_y = 6
        self.board = board
        self.players = []
        self.dice = 0
        #player_id enlevé ici de init

    def roll_dice(self):
        # tirer au sort un nombre entre 1 et 6
        dice_number = random.choice(range(1,7))
        print("")
        print ("resultat du dé: ", dice_number)
        print("")
        return dice_number


    def choose_move(self):
        pass


    def answer_question(self):
        #return self.board.ask_question() ici teste True
        return True


    def show_available_cells(self):

        dico_available_cells = {}
        set_cells = set()
        
        # variables pour tester si on obtient les bonnes coordonnées
        dice_number = self.dice
        self.col = self.y
        self.row = self.x
        

        # si on est sur la première ligne on peut aller à gauche et à droite
        # mais si position + dé est inférieur à 0 ou supérieur à 12
        # alors on ajoute la diff à self.col 

        if self.row == 0:

            # déplacement à gauche sur une ligne
            if self.col - dice_number >= 0:
                #print(f"{(self.row, self.col - dice_number)}")
                set_cells.add((self.row, self.col - dice_number))

            # si jamais "index out of range" alors on ajoute la différence restante à self.row
            else:
                diff = abs(self.col - dice_number)
                #print(f"{(self.row + diff, 0)}")
                set_cells.add((self.row + diff, 0))

            # déplacement à droite sur une ligne
            if self.col + dice_number <= 12:
                #print(f"{(self.row, self.col + dice_number)}")
                set_cells.add((self.row, self.col + dice_number))

            # si jamais "index out of range" alors on ajoute la différence restante à self.row    
            else:
                diff = abs(12-(self.col + dice_number))
                #print(f"{self.row+diff, 12}")
                set_cells.add((self.row+diff, 12))



        if self.row == 12:

            # déplacement à gauche sur une ligne
            if self.col - dice_number >= 0:
                #print(f"{(self.row, self.col - dice_number)}")
                set_cells.add((self.row, self.col - dice_number))
                
            # si jamais "index out of range" alors on soustrait la différence restante à self.row pour 
            else:
                diff = abs(self.col - dice_number)
                #print(f"{(self.row - diff, 12)}")
                set_cells.add((self.row - diff, 12))

            # déplacement à droite sur une ligne
            if self.col + dice_number <= self.width:
                #print(f"{(12, self.col + dice_number)}")
                set_cells.add((12, self.col + dice_number))

            # si jamais "index out of range" alors l
            else:
                diff = abs(12 - (dice_number + self.col))
                #print(f"{(self.row-diff, 12)}")
                set_cells.add((self.row-diff, 12))


        if self.row == 6:

            # déplacement à gauche
            if self.col - dice_number >= 0:
                #print(f"{(self.row, self.col-dice_number)}")
                set_cells.add((self.row, self.col-dice_number))

            elif self.col - dice_number <= 0 and self.col != 0:
                diff = abs(self.col - dice_number)
                #print(f"{(0, abs(self.col-diff))}")
                #print(f"{(0, self.col+diff)}")
                set_cells.add((0, abs(self.col-diff)))
                set_cells.add((0, self.col+diff))

            if self.col + dice_number <= 12:
                #print(f"{(self.row, self.col+dice_number)}")
                set_cells.add((self.row, self.col+dice_number))

            else:
                diff = abs(12 -(self.col+dice_number))
                #print(f"{(self.row-diff,12)}")
                #print(f"{(self.row+diff, 12)}")
                set_cells.add((self.row-diff,12))
                set_cells.add((self.row+diff, 12))


        
        if self.col == 0:

            #déplacement en haut
            if self.row - dice_number >= 0:
                #print(f"{(self.row-dice_number, self.col)}")
                set_cells.add((self.row-dice_number, self.col))

            else:
                diff = abs(self.row - dice_number)
                #print(f"{(0, self.col + diff)}")
                set_cells.add((0, self.col + diff))

            #déplacement en bas
            if self.row + dice_number <= 12:
                #print(f"{(self.row+dice_number, self.col)}")
                set_cells.add((self.row+dice_number, self.col))
            else:
                diff = abs(12-(self.row+dice_number))
                #print(f"{(12, self.col + diff)}")
                set_cells.add((12, self.col + diff))


        if self.col == 12:

            # déplacement en haut
            if self.row - dice_number >= 0:
                #print(f"{(self.row - dice_number, 12)}")
                set_cells.add((self.row - dice_number, 12))

            else:
                diff = abs(self.row - dice_number)
                #print(f"{(0, self.col - diff)}")
                set_cells.add((0, self.col - diff))

            # déplacement en bas
            if self.row + dice_number <= 12:
                #print(f"{(self.row+dice_number, self.col)}")
                set_cells.add((self.row+dice_number, self.col))

            else:
                diff = abs(12 - (self.row + dice_number))
                #print(f"{(12, self.col - diff)}")
                set_cells.add((12, self.col - diff))


        if self.col == 6:

            # déplacement en haut
            if self.row - dice_number >= 0:
                #print(f"{(self.row-dice_number, self.col)}")
                set_cells.add((self.row-dice_number, self.col))
            else:
                diff = abs(self.row-dice_number)
                #print(f"{(0, self.col-diff)}")
                #print(f"{(0, self.col+diff)}")
                set_cells.add((0, self.col-diff))
                set_cells.add((0, self.col+diff))

            if self.row + dice_number <= 12:
                #print(f"{(self.row+dice_number, self.col)}")
                set_cells.add((self.row+dice_number, self.col))
            else:
                diff = abs(12-(self.row+dice_number))
                # print(f"{(12, self.col - diff)}")
                # print(f"{(12, self.col + diff)}")
                set_cells.add((12, self.col - diff))
                set_cells.add((12, self.col + diff))
            

        j = 0    
        for i in set_cells:
            j += 1
            dico_available_cells[j] = i

        for i,j in dico_available_cells.items():
            print(f"Choix {i} : {j}")

        print("")
        user_choice = input("Merci de taper le chiffre correspondant à la case où vous souhaitez vous déplacer : ")

        # Vérifie si l'entrée de l'utilisateur est un nombre et est une clé valide dans dico_available_cells
        while user_choice not in map(str, dico_available_cells.keys()):
            user_choice = input("Merci de taper le chiffre correspondant à la case où vous souhaitez vous déplacer : ")

        # print(f"Vous avez choisi cette destination : {user_choice}")
        print("")

        return dico_available_cells[int(user_choice)]   #récupère les coordonnées choisies par notre joueur

    def move(self):

        print(f"Tour de {self.name} {self.token}")
        print("")
        self.dice = self.roll_dice()
        # Change la couleur de l'ancienne case pour celle de départ
        if self.y == 6 and self.x == 6:
            self.board.grid[self.x][self.y] = "⬜️"
        else:
            self.board.grid[self.x][self.y] = self.case_color

        # Change les positions de new x,y pour celle de la case choisie
        self.future_cell = self.show_available_cells()

        while self.board.grid[self.future_cell[0]][self.future_cell[1]] not in self.perfect_score:
            print("Choix indisponible, réessayer")
            self.future_cell = self.show_available_cells()

        self.new_x, self.new_y = self.future_cell[0], self.future_cell[1]

        # Sauvegarde la couleur de la case choisie
        self.case_color = self.board.grid[self.new_x][self.new_y]

        # Doublon 
        self.color_of_question = self.board.grid[self.new_x][self.new_y]

        self.board.grid[self.new_x][self.new_y] = self.token

        self.x, self.y = self.new_x, self.new_y
    
    def upgrade_score(self):
        if self.answer_question():
            self.score += 1
        return self.score
    
    def show_score(self):
        #return self.score
        score = ""
        for i in range(6):
            if self.score[i] != 0:
                score += self.perfect_score[i]
            else:
                score += "⬛️"
        print(self.token + " " + score)
        print("")
    



# board1 = Board(12, 12, 3)
# board1.create_boardgame()
# #game1 = Game(2, board1)
# #print(game1.players[0].name, game1.players[0].token)
# ##print(game1.players[1].name, game1.players[1].token)
# board1
# player1 = Player(board1)
# player1.move()
