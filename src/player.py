from random import *
#from board import *
from src.game import *
#attention, ici tests sont inclus ainsi que les modifs liées aux fonctions deplacées depuis board
import networkx as nx

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
    
    
    def show_available_cells_graph(self, G, dice_result, current_position):
        paths = nx.single_source_shortest_path_length(G, current_position, cutoff=dice_result)
        nodes_to_go = [node for node, distance in paths.items() if distance == dice_result]
        return nodes_to_go


    def create_graph(self):
        # Créer un graphe vide
        G = nx.Graph()

        n_ext = 48
        n_total = 69

        # Création du cercle extérieur
        for i in range(0, n_ext):
            G.add_node(i)

        # Création des arrêtes extérieurs
        for i in range(0, n_ext-1):
            G.add_edge(i, i + 1)

        # La boucle est bouclée
        G.add_edge(n_ext-1, 0)

        # Création des chemins intérieurs
        for i in range(n_ext, n_total):
            G.add_node(i)

        centre = 53

        # Branche 1
        for i in range(48, 58):
            G.add_edge(i, i + 1)

        # Branche 2
        for i in range(59, 64):
            G.add_edge(i, i + 1)

        # Branche 2 bis
        for i in range(64, 69):
            G.add_edge(i, i + 1)

        # Connexions spéciales à l'extérieur
        G.add_edge(6, 59)
        G.add_edge(18, 58)
        G.add_edge(30, 68)
        G.add_edge(42, 48)

        # Connexions spéciales à l'intérieur
        G.add_edge(centre, 63)
        G.add_edge(centre, 64)

        return G

    
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
