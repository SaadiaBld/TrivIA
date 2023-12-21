from random import *
#from board import *
from src.game import *
#attention, ici tests sont inclus ainsi que les modifs liées aux fonctions deplacées depuis board



class Player:
    def __init__(self, board):
        tokens = ["🦊","🐨","🐼","🐸","🐱"]
        self.name = input(f"What's your name?: ")
        self.token = random.choice(tokens)
        self.score = [0,0,0,0,0,0]
        self.x = board.col
        self.y = board.row_middle
        self.new_x = None
        self.new_y = None
        self.board = board
        self.players = []
        #player_id enlevé ici de init

    def roll_dice(self):
        # tirer au sort un nombre entre 1 et 6
        dice_number = random.choice(range(1,7))
        return dice_number
        print ("resultat dé:", dice_number)

    def choose_move(self):
        pass


    def answer_question(self):
        #return self.board.ask_question() ici teste True
        return True



        
    
    def show_available_cells(self):

        dico_available_cells = {}
        set_cells = set()
        
        # variables pour tester si on obtient les bonnes coordonnées
        dice_number = 4
        self.col = 12
        self.row = 6
        

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

            else:
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

        print(dico_available_cells)

        user_choice = int(input("Merci de taper le chiffre correspondant à la case où vous souhaitez vous déplacer : "))
        print(f"Vous avez choisi cette destination : {user_choice}")
    
        return dico_available_cells[user_choice]   #récupère les coordonnées choisies par notre joueur       
    

    def move(self):
        if self.y == 6 and self.x == 6 and self.answer_question():
            self.board.grid[self.x][self.y] = "⬜️"
        else:
            self.board.grid[self.x][self.y] = color

        future_cell = self.show_available_cells_graph()
        self.new_y, self.new_x = future_cell[0], future_cell[1]

        color = self.board.grid[self.new_x][self.new_y] # cell where player will go
        color

        self.board.grid[self.y][self.x] = self.token

        self.y, self.x = self.new_y, self.new_x

    #def update_position(self):
        old_value = self.board.grid[self.y][self.x]
        #if self.answer_question():
        self.board.grid[self.y][self.x]=old_value
        self.board.grid[self.new_y][self.new_x] = self.token
    
    def upgrade_score(self):
        if self.answer_question():
            self.score += 1
        return self.score
    
    def show_score(self):
        return self.score
    

    
    def move(self, grid):

        if self.row == 6 and self.col == 6:
            self.grid[self.row][self.col] = "⬜️"
        else:
            self.grid[self.row][self.col] = color

        future_cell = self.show_available_cells()
        new_row, new_col = future_cell[0], future_cell[1]

        color = self.grid[new_row][new_col]  # cell where player will go
        color

        # remplacer la couleur par l'émoji du joueur
        self.grid[self.row][self.col] = self.token
