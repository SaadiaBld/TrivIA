import random
import pandas as pd
from db import read_table

class Board():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.col = int(width/2)
        self.row = int(height/2)
        self.user_answer = 0
        self.correct_answer = 0
        self.score = []
        self.dico_score = {}
        self.numbers_of_players
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
                 

        # dé 3D? comment animer un .obj en python?
        # dé 3D? animations Blender
        # images des faces d'un dé?
    
    
    def check_player_position(self, grid, dice_number):
        
        # sauvegarder la position actuelle du joueur
        pass
    
    
    def show_available_cells(self):
        
        
        def roll_dice():
        # tirer au sort un nombre entre 1 et 6
            dice_number = random.choice(range(1,7))
            return dice_number
        

        dico_available_cells = {}
        set_cells = {}


        
        # ABOVE
        
        # possibilité dans la même colonne (plus haut)
        
        #if self.row-1 is not False:
            
        # déplacement normal sur les cellules au dessus (indices de lignes inférieurs)
        if self.grid[self.col][self.row-1] != "⬛️":
            if self.row - self.roll_dice() >= 0:

                #print(f"{(self.row - dice_number, self.col)}")
                set_cells.add((self.row - self.roll_dice(), self.col))




        if self.grid[self.col-1][self.row] != "⬛️":
            if self.col < self.height:
                #print(f"{self.row, (self.col + dice_number)}")
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
    
        return dico_available_cells[user_choice]   #récupère les coordonnées choisies par notre joueur


    def move(self, grid):
        
        coord = self.show_available_cells
        cell_where_player_will_go = grid[self.dico_available_cells[self.user_choice][0]][self.dico_available_cells[self.user_choice][1]]
        
        new_row = self.dico_available_cells[self.user_choice][0]
        new_col = self.dico_available_cells[self.user_choice][1]

        if self.row == 6 and self.col == 6:
            start = "⬜️" #ou = 14
            self.grid[self.row][self.col] = start
            self.row, self.col = new_row, new_col
            self.grid[self.row][self.col] == self.token
        else:
            # self.grid[self.row][self.col] == cell_where_player_will_go
            self.row, self.col = new_row, new_col
            self.grid[self.row][self.col] == self.token







        



    def move(self):
        
        #position avant: self.x, self.y
        #position aprés



    def show_title(self):
                return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       TRIVIA PURSUIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━""" 



    def ask_question(self):

        self.ids = [] # à mettre dans le init de la classe

        self.score = ["⬛️","⬛️","⬛️","⬛️","⬛️"]

        self.categories = {"0": [0, "⬛️", 0],
                                "1": ["python", "🟩"],
                                "2": ["sql", "🟪"],
                                "3": ["git", "🟨"],
                                "4": ["terminal", "🟥"],
                                "5": ["actu_ia", "🟦"],
                                "6": ["soft_skills", "🟧"],
                                "7": ["python", "🟩"],
                                "8": ["soft_skills", "🟧"],
                                "9": ["actu_ia", "🟦"],
                                "10": ["terminal", "🟥"],
                                "11": ["git", "🟨"],
                                "12": ["sql", "🟪"],
                                "13": ["python", "🟩"],
                                "14": ["start", "⬜️"]}

        # categories["1"][0]

        # retourne la catégorie de la case sur laquelle le joueur se trouve
        categ = self.categories[str(self.col)][0]

        dictionnaire_avec_question = read_table(categ, self.ids)
        # print(dictionnaire_avec_question)
        self.ids.append(dictionnaire_avec_question["id"])

        # afficher la question (sortie de manière aléatoire via SQL)
        print(dictionnaire_avec_question["question"])

        # randomiser et afficher les réponses (pour éviter que ce soit toujours la réponse A la réponse correcte)
        i = 0
        for j in random.sample(["correct_answer", "incorrect_answer_1", "incorrect_answer_2", "incorrect_answer_3"], 4):
                i+=1
                print(f"{i}. {dictionnaire_avec_question[j]}")
                
                if j == "correct_answer":
                    self.correct_number = i

        # demander de choisir une réponse à l'utilisateur
        self.user_answer = input("Merci de taper le chiffre correspondant à la réponse que vous souhaitez donner : ")

        if int(self.user_answer) == self.correct_number:

            print("Bravo! Bonne réponse")
            
            if self.categories[str(self.col)][1] not in self.score:
                self.score = self.score.pop()
                self.score = self.score.append(self.categories[str(self.col)][1])
            else:
                pass

        else:

            print("Raté.")



    def update_score(self):

        # besoin de la variable nombre_de_joueurs pour générer leurs scores respectifs

        for i in range(1, self.numbers_of_players+1):
            self.dico_score.update({f"player {i}" : self.score})


        for i in self.dico_score:
            while len(self.dico_score[i]) < 6:
                self.dico_score[i].append("⬛️")


        #if int(self.user_answer) == self.correct_number and "🟩" not in self.score:
        if int(self.user_answer) == self.correct_number and self.categories[str(self.col)][1] not in self.score:
            self.score.pop()
            self.score.insert(0, self.categories[str(self.col)][1])

        else:
            pass

        print(f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    CLASSEMENT DES JOUEURS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

        for key,value in self.dico_score.items():
            print(f"{key} : {''.join(value)}")



    # def sort_score():

    #     def show_score(element):
    #         return len(element)

    #     list_of_scores = [["🟩", "🟪", "🟨", "🟥", "🟦"], ["🟪","🟩"], ["🟨", "🟩", "🟪"], []]

    #     list_of_scores_sorted = sorted(list_of_scores, key=show_score, reverse=True)

    #     for i in list_of_scores_sorted:
    #         while len(i) < 5:
    #             i.append("⬛️")

    #     print(f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # CLASSEMENT DES JOUEURS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

    #     j = 0

    #     for i in list_of_scores_sorted:
    #         j += 1
    #         print(f'Player #{j} {"".join(i)}')




# boardgame = Board(12,12) #taille maximale pour le moment, il faut optimiser la taille dans la méthode de la classe Grid
# title = boardgame.show_title()
# print(title)
# boardgame.create_boardgame()
# score_result = boardgame.show_score()
# print(score_result)
# boardgame.show_available_cells()
# boardgame.ask_question()

        for i in random.sample([4,5,6,7], 4):
            print(dictionnaire_avec_question[i])
                 
            

# boardgame.sort_score()
# boardgame.update_score()