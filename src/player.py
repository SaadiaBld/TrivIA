from random import *
#from board import *
from game import *
#attention, ici tests sont inclus ainsi que les modifs liées aux fonctions deplacées depuis board
class Board():

    def __init__(self, width, height, numbers_of_players): #j'ai ajouté numberofplayers ici
        self.width = width
        self.height = height
        self.col = int(width/2)
        self.row_middle = int(height/2)  #renommé self.row en self.row_middle pr eviter conflits avec self.row
        self.user_answer = 0
        self.correct_answer = 0
        self.score = []
        self.dico_score = {}
        self.numbers_of_players = numbers_of_players
        self.row = [str(i+1) for i in range(0, self.width+1)]
        self.grid = [list(self.row) for j in range(0, self.height+1)]



    def create_boardgame(self):

        # Création des lignes (avec des nombres de 1 à 11)
        row = [str(i+1) for i in range(0, self.width+1)]

        # Création de la grille (ajout de colonnes)
        grid = [list(row) for j in range(0, self.height+1)]
        self.grid = grid

        # Ajout de valeurs 0 "False" sur lesquelles on ne peut pas jouer
        for i in range(1,12): # ce range = columns
            for index in range(1,6):
                grid[i][index] = "0"
            for index in range(7, 12):
                grid[i][index] = "0"


        # Dictionnaire des catégories avec leurs couleurs correspondantes
        categories = {"0": [0, "⬛️", 0],
                        "1": ["python", "🟩", 1],
                        "2": ["sql", "🟪", 2],
                        "3": ["git", "🟨", 3],
                        "4": ["terminal", "🟥", 4],
                        "5": ["actu_ia", "🟦", 5],
                        "6": ["soft_skills", "🟧", 6],
                        "7": ["python", "🟩", 1],
                        "8": ["soft_skills", "🟧", 6],
                        "9": ["actu_ia", "🟦", 5],
                        "10": ["terminal", "🟥", 4],
                        "11": ["git", "🟨", 3],
                        "12": ["sql", "🟪", 2],
                        "13": ["python", "🟩", 1],
                        "14": ["start", "⬜️", 0]}
        
        
        
        # Modification de la ligne du milieu de la grille
        grid[6] = grid[0].copy()
        
        # Modification des colonnes 0, 5 et -1
        # (elles affichaient une seule et unique valeur, maintenant elles s'affichent comme les lignes)    
        for row_index in range(len(grid)):
            grid[row_index][0] = str(row_index + 1)
            grid[row_index][-1] = str(row_index + 1)
            grid[row_index][6] = str(row_index + 1)
        
            
        # Modification des nombres dans la grille avec les couleurs correspondantes
        for row in grid:
            for col_index in range(len(row)):
                number = row[col_index]
                if number in categories:
                    row[col_index] = categories[number][1]
                    
        
        # DIAGONALES
        # Création des diagonales
        for i in range(1, 12):
            grid[i][i] = categories[str(i+1)][1]
            grid[i][self.width - i] = categories[str(self.width - i + 1)][1]
            
                
        # Modification du centre de la grille    #START
        grid[6][6] = categories["14"][1]
        
        
        # test d'affichage
        old_value = grid[7][12]
        #grid[7][12] = "X"
        old_value


        # Affichage de la grille 
        for row in grid:
            print("".join(row))
    
    '''def show_available_cells(self):
        
        
        def roll_dice():
            return random.choice(range(1,7))
        

        dico_available_cells = {}
        set_cells = {}


        
        # ABOVE
        
        # possibilité dans la même colonne (plus haut)
        
        #if self.row-1 is not False:
            
        # déplacement normal sur les cellules au dessus (indices de lignes inférieurs)
        if self.y - 1 >= 0 and self.grid[self.y - 1][self.x] != "⬛️":
        #if self.grid[self.col][self.row-1] != "⬛️":
            if self.y - self.roll_dice() >= 0:

                #print(f"{(self.row - dice_number, self.col)}")
                set_cells.add((self.y - self.roll_dice(), self.x))




        if self.y < self.height and self.grid[self.y + 1][self.x] != "⬛️":
            if self.y + self.roll_dice() < self.height:                #print(f"{self.row, (self.col + dice_number)}")
                set_cells.add((self.row, (self.col + self.roll_dice())))


            else:
                #print(f"{self.row, (self.col - dice_number)}")
                set_cells.add((self.row, (self.col - self.roll_dice())))


            
            difference = abs(self.roll_dice() - self.col)
            #difference = dice_number - self.col
            
            if (self.width-self.col)-(difference-self.row) < self.width:
                set_cells.add((self.row+difference, 0))
                #print(f"{(self.row+difference, 0)}")
            
            if self.row < self.height and self.width-(self.row+difference) < self.height:
                set_cells.add((self.row+difference, 0))
                # print(f"{(self.row+difference, 0)}")
                # print(f"{(self.col, self.width-(self.row+difference))}")
            
            
        # self.row = 7
        # self.col = 12
            
        # si jamais on arrive à la toute première ligne, on peut virer à gauche et à droite
        if self.row - self.roll_dice() < 0: #and self.row != 6:
            
            difference = self.roll_dice() - self.row
            
            self.col_right = self.col + difference
            self.col_left = self.col - difference
            
            if self.width > self.col_right > 0:
                set_cells.add((0, self.col_right))
                #print(f"{(0, self.col_right)}") # possibilité à droite
                
            if self.col_left > 0:
                set_cells.add((0, self.col_left))
                # print(f"{(0, self.col_left)}") # possibilité à gauche
                
        
        # self.row = 7
        # self.col = 12
        
        #BELOW 
        
        if self.row < self.height-1:
            if self.grid[self.col][self.row+1] != "⬛️" and self.row < self.height:
                if self.row + self.roll_dice() <= self.height:
                    set_cells.add((self.row + self.roll_dice(), self.col))
                    # print(f"{(self.row + dice_number, self.col)}")
            
        
            if self.row + self.roll_dice() > self.width and self.grid[self.col][self.row+1] != "⬛️":
                
                difference = (self.roll_dice() + self.row) - self.width
                
                # self.row = 12
                self.col_right = self.col + difference
                self.col_left = self.col - difference
                
                if self.width > self.col_right > 0:
                    set_cells.add((12, self.col_right))
                    #print(f"{(12, self.col_right)}") # possibilité à droite
                    
                if self.col_left > 0:
                    set_cells.add(((12, self.col_left)))
                    #print(f"{(12, self.col_left)}") # possibilité à gauche
                
            
        j = 0    
        for i in set_cells:
            j += 1
            dico_available_cells[j] = i

        for i,j in dico_available_cells.items():
            print(f"Choix {i} : {j}")

        user_choice = int(input("Merci de taper le chiffre correspondant à la case où vous souhaitez vous déplacer : "))
        print(f"Vous avez choisi cette destination : {user_choice}")
    
        return dico_available_cells[user_choice]'''
    
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


        
        # ABOVE
        
        # possibilité dans la même colonne (plus haut)
        
        #if self.row-1 is not False:
            
        # déplacement normal sur les cellules au dessus (indices de lignes inférieurs)
        if self.y - 1 >= 0 and self.board.grid[self.y - 1][self.x] != "⬛️":
        #if self.grid[self.col][self.row-1] != "⬛️":
            if self.y - self.roll_dice() >= 0:

                #print(f"{(self.row - dice_number, self.col)}")
                set_cells.add((self.y - self.roll_dice(), self.x))




        if self.y < self.board.height and self.board.grid[self.y + 1][self.x] != "⬛️":
            if self.y + self.roll_dice() < self.board.height:                #print(f"{self.row, (self.col + dice_number)}")
                set_cells.add((self.y, (self.x + self.roll_dice())))


            else:
                #print(f"{self.row, (self.col - dice_number)}")
                set_cells.add((self.y, (self.x - self.roll_dice())))


            
            difference = abs(self.roll_dice() - self.x)
            #difference = dice_number - self.col
            
            if (self.board.width-self.x)-(difference-self.y) < self.board.width:
                set_cells.add((self.y + difference, 0))
                #print(f"{(self.row+difference, 0)}")
            
            if self.y < self.board.height and self.board.width-(self.y+difference) < self.board.height:
                set_cells.add((self.y + difference, 0))
                # print(f"{(self.row+difference, 0)}")
                # print(f"{(self.col, self.width-(self.row+difference))}")
            
            
        # self.row = 7
        # self.col = 12
            
        # si jamais on arrive à la toute première ligne, on peut virer à gauche et à droite
        if self.y - self.roll_dice() < 0: #and self.row != 6:
            
            difference = self.roll_dice() - self.y
            
            self.col_right = self.x + difference
            self.col_left = self.x - difference
            
            if self.board.width > self.col_right > 0:
                set_cells.add((0, self.col_right))
                #print(f"{(0, self.col_right)}") # possibilité à droite
                
            if self.col_left > 0:
                set_cells.add((0, self.col_left))
                # print(f"{(0, self.col_left)}") # possibilité à gauche
                
        
        # self.row = 7
        # self.col = 12
        
        #BELOW 
        
        if self.y < self.board.height-1:
            if self.board.grid[self.y][self.x+1] != "⬛️" and self.y < self.board.height:
                if self.y + self.roll_dice() <= self.board.height:
                    set_cells.add((self.y + self.roll_dice(), self.x))
                    # print(f"{(self.row + dice_number, self.col)}")
            
        
            if self.y + self.roll_dice() > self.board.width and self.board.grid[self.x][self.y+1] != "⬛️":
                
                difference = (self.roll_dice() + self.y) - self.board.width
                
                # self.row = 12
                self.col_right = self.x + difference
                self.col_left = self.x - difference
                
                if self.board.width > self.col_right > 0:
                    set_cells.add((12, self.col_right))
                    #print(f"{(12, self.col_right)}") # possibilité à droite
                    
                if self.col_left > 0:
                    set_cells.add(((12, self.col_left)))
                    #print(f"{(12, self.col_left)}") # possibilité à gauche
                
            
        j = 0    
        for i in set_cells:
            j += 1
            dico_available_cells[j] = i

        for i,j in dico_available_cells.items():
            print(f"Choix {i} : {j}")

        print(self.roll_dice())
        user_choice = int(input("Merci de taper le chiffre correspondant à la case où vous souhaitez vous déplacer : "))
        print(f"Vous avez choisi cette destination : {user_choice}")
    
        return dico_available_cells[user_choice]

    def move(self):
        if self.y == 6 and self.x == 6 and self.answer_question():
            self.board.grid[self.x][self.y] = "⬜️"
        else:
            self.board.grid[self.x][self.y] = color

        future_cell = self.show_available_cells()
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
    



board1 = Board(12, 12, 3)
board1.create_boardgame()
#game1 = Game(2, board1)
#print(game1.players[0].name, game1.players[0].token)
##print(game1.players[1].name, game1.players[1].token)
board1
player1 = Player(board1)
player1.move()
