import random
#from board import *
# from src.game import *
#attention, ici tests sont inclus ainsi que les modifs liées aux fonctions deplacées depuis board
    
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


        
        # ABOVE
        
        # possibilité dans la même colonne (plus haut)
        
        #if self.row-1 is not False:
            
        # déplacement normal sur les cellules au dessus (indices de lignes inférieurs)
        if self.y - 1 >= 0 and self.board.grid[self.y - 1][self.x] != "⬛️":
        #if self.grid[self.col][self.row-1] != "⬛️":
            if self.y - self.dice >= 0:

                #print(f"{(self.row - dice_number, self.col)}")
                set_cells.add((self.y - self.dice, self.x))




        if self.y < self.board.height and self.board.grid[self.y + 1][self.x] != "⬛️":
            if self.y + self.dice < self.board.height:                #print(f"{self.row, (self.col + dice_number)}")
                set_cells.add((self.y, (self.x + self.dice)))


            else:
                #print(f"{self.row, (self.col - dice_number)}")
                set_cells.add((self.y, (self.x - self.dice)))


            
            difference = abs(self.dice - self.x)
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
        if self.y - self.dice < 0: #and self.row != 6:
            
            difference = self.dice - self.y
            
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
                if self.y + self.dice <= self.board.height:
                    set_cells.add((self.y + self.dice, self.x))
                    # print(f"{(self.row + dice_number, self.col)}")
            
        
            if self.y + self.dice > self.board.width and self.board.grid[self.x][self.y+1] != "⬛️":
                
                difference = (self.dice + self.y) - self.board.width
                
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

        print(self.dice)
        user_choice = int(input("Merci de taper le chiffre correspondant à la case où vous souhaitez vous déplacer : "))
        print(f"Vous avez choisi cette destination : {user_choice}")
    
        return dico_available_cells[user_choice]

    def move(self):

        self.dice = self.roll_dice()
        if self.y == 6 and self.x == 6:# and self.answer_question():
            self.board.grid[self.x][self.y] = "⬜️"
        else:
            self.board.grid[self.x][self.y] = self.color

        self.color = self.board.grid[self.new_x][self.new_y] # cell where player will go


        self.future_cell = self.show_available_cells()
        self.new_x, self.new_y = self.future_cell[0], self.future_cell[1]


        self.color_of_question = self.board.grid[self.new_x][self.new_y]

        self.board.grid[self.x][self.y] = self.token

        self.x, self.y = self.new_x, self.new_y

    #def update_position(self):
        old_value = self.board.grid[self.x][self.y]
        #if self.answer_question():
        self.board.grid[self.x][self.y]=old_value
        self.board.grid[self.new_x][self.new_y] = self.token
    
    def upgrade_score(self):
        if self.answer_question():
            self.score += 1
        return self.score
    
    def show_score(self):
        #return self.score
        score
        for i in range(6):
            if self.score[i] != 0:
                score += self.perfect_score[i]
            else:
                score += "⬛️"
        print(score)
        return ("OUI")
    



# board1 = Board(12, 12, 3)
# board1.create_boardgame()
# #game1 = Game(2, board1)
# #print(game1.players[0].name, game1.players[0].token)
# ##print(game1.players[1].name, game1.players[1].token)
# board1
# player1 = Player(board1)
# player1.move()
