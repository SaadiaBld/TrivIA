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
        
        dice_number = self.dice
        
        self.col = self.x
        self.row = self.y
        
        # ABOVE
        
        if self.board.grid[self.col][self.row-1] != "⬛️":
            if 12 >= (self.row - dice_number) >= 0:
                # print(f"{(self.col, self.row - dice_number)}")
                set_cells.add((self.col, self.row - dice_number))

                if self.row != self.board.height and self.board.grid[self.col][self.row+1] != "⬛️" and self.row+1 < self.board.height:
                    # print(f"{(self.row - dice_number, self.col)}")
                    set_cells.add((self.row - dice_number, self.col))

                    #print(f"{(self.row + dice_number, self.col)}")

                if self.col == 6 and self.row == 6:
                    # print(f"{(self.row - dice_number, self.col)}")
                    set_cells.add((self.row - dice_number, self.col))
                    # print(f"{(self.row + dice_number, self.col)}")
                    set_cells.add((self.row + dice_number, self.col))
            
        if self.board.grid[self.col-1][self.row] != "⬛️": # and self.col+1 > self.height:
            if self.col < self.board.height:
                # print(f"{self.col + dice_number, self.row}")
                set_cells.add((self.col + dice_number, self.row))

            if self.col - dice_number < 0:
                diff = abs(self.col-dice_number)
                # print(f"{0, self.row+diff}")
                set_cells.add((0, self.row+diff))
            else:
                # print(f"{(abs(self.col - dice_number)), self.row}")
                set_cells.add((abs(self.col - dice_number), self.row))


            
        # si jamais on arrive à la toute première ligne, on peut virer à gauche et à droite
        if self.row - dice_number < 0: #and self.row != 6:
            
            difference = dice_number - self.row
            
            self.col_right = self.col + difference
            self.col_left = self.col - difference
            
            if self.width > self.col_right >= 0:
                # print(f"{(self.col_right, 0)}") # possibilité à droite
                set_cells.add((self.col_right, 0))
                
            if self.col_left >= 0:
                # print(f"{(self.col_left, 0)}") # possibilité à gauche
                set_cells.add((self.col_left, 0))
                
        
        # self.col = 3
        # self.row = 0
        
        # # #BELOW 
        
        if self.row < self.board.height-1:
            if self.board.grid[self.col][self.row+1] != "⬛️":
                if self.row + dice_number <= self.board.height:
                    # print(f"{(self.col, self.row + dice_number)}")
                    set_cells.add((self.col, self.row + dice_number))
                    
                    if self.col + dice_number < self.board.height:
                        # print(f"{(self.col + dice_number, self.row)}")
                        set_cells.add((self.col + dice_number, self.row))
            
        
            if self.row + dice_number > self.board.width and self.board.grid[self.col][self.row+1] != "⬛️":
                
                difference = (dice_number + self.row) - self.board.width
                
                self.row = 12
                self.col_right = self.col + difference
                self.col_left = self.col - difference
                
                if self.board.width > self.col_right > 0:
                    # print(f"{(self.col_right, self.row)}") # possibilité à droite
                    set_cells.add((self.col_right, self.row))
                    
                if self.col_left > 0:
                    # print(f"{(self.col_left, self.row)}") # possibilité à gauche
                    set_cells.add((self.col_left, self.row))

        j = 0    
        for i in set_cells:
            j += 1
            dico_available_cells[j] = i

        for i,j in dico_available_cells.items():
            print(f"Choix {i} : {j}")

        print("Le resultat du dé est : " + str(self.dice))
        user_choice = int(input("Merci de taper le chiffre correspondant à la case où vous souhaitez vous déplacer : "))
        print(f"Vous avez choisi cette destination : {user_choice}")
    
        return dico_available_cells[user_choice]


    
    
    def show_available_cells_graph(self, G, dice_result, current_position):
        dico_available_cells = {}
        paths = nx.single_source_shortest_path_length(G, current_position, cutoff=dice_result)
        nodes_to_go = [node for node, distance in paths.items() if distance == dice_result]

        # Chemin du fichier JSON
        chemin_fichier_json = 'src/mapping_coor.json'

        # Charger le JSON depuis le fichier et le convertir en dictionnaire
        with open(chemin_fichier_json, 'r') as fichier:
            dict_mapping = json.load(fichier)

        j = 0    
        for i in nodes_to_go:
            j += 1
            dico_available_cells[j] = dict_mapping.get(str(i))

        for i,j in dico_available_cells.items():
            print(f"Choix {i} : {j}")

        print(self.roll_dice())
        user_choice = int(input("Merci de taper le chiffre correspondant à la case où vous souhaitez vous déplacer : "))
        print(f"Vous avez choisi cette destination : {user_choice}")
    
        return dico_available_cells[user_choice]

    def move(self, G, dice_result, current_position):

        self.dice = self.roll_dice()

        # Change la couleur de l'ancienne case pour celle de départ
        if self.y == 6 and self.x == 6:
            self.board.grid[self.x][self.y] = "⬜️"
        else:
            self.board.grid[self.x][self.y] = self.case_color

        # Change les positions de new x,y pour celle de la case choisie
        self.future_cell = self.show_available_cells_graph(G, dice_result, current_position)
        print(self.future_cell[0]) 
        print(self.future_cell[1])
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
        print(score)
    



# board1 = Board(12, 12, 3)
# board1.create_boardgame()
# #game1 = Game(2, board1)
# #print(game1.players[0].name, game1.players[0].token)
# ##print(game1.players[1].name, game1.players[1].token)
# board1
# player1 = Player(board1)
# player1.move()
