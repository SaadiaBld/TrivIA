import random

class Board():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.col = int(width/2)
        self.row = int(height/2)
        
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
                 
            
    def roll_dice():
        # tirer au sort un nombre entre 1 et 6
        dice_number = random.choice(range(1,7))
        return dice_number
    
        # dé 3D? comment animer un .obj en python?
        # dé 3D? animations Blender
        # images des faces d'un dé?
    
    
    def check_player_position(self, grid, dice_number):
        
        # sauvegarder la position actuelle du joueur
        pass
    
    
    def show_available_cells(self):
        
        dice_number = 6
        
        self.row = 7
        self.col = 12
        
        # ABOVE
        
        # possibilité dans la même colonne (plus haut)
        
        #if self.row-1 is not False:
        if self.grid[self.col][self.row-1] != "⬛️":
            if self.row - dice_number >= 0:
                print(f"{(self.row - dice_number, self.col)}")
            
        if self.grid[self.col-1][self.row] != "⬛️":
            if self.col < self.height:
                print(f"{self.row, (self.col + dice_number)}")
            else:
                print(f"{self.row, (self.col - dice_number)}")
            
            difference = abs(dice_number - self.col)
            difference = dice_number - self.col
            self.col = 0
            
            if (self.width-self.col)-(difference-self.row) < self.width:
                print(f"{(self.row+difference, self.col)}")
            
            if self.row < self.height and self.width-(self.row+difference) < self.height:
                print(f"{(self.row+difference, self.col)}")
                # print(f"{(self.col, self.width-(self.row+difference))}")
            
            
        self.row = 7
        self.col = 12
            
        # si jamais on arrive à la toute première ligne, on peut virer à gauche et à droite
        if self.row - dice_number < 0: #and self.row != 6:
            
            difference = dice_number - self.row
            
            self.col_right = self.col + difference
            self.col_left = self.col - difference
            
            if self.width > self.col_right > 0:
                print(f"{(0, self.col_right)}") # possibilité à droite
                
            if self.col_left > 0:
                print(f"{(0, self.col_left)}") # possibilité à gauche
                
        
        self.row = 7
        self.col = 12
        
        #BELOW 
        
        if self.row < self.height-1:
            if self.grid[self.col][self.row+1] != "⬛️" and self.row < self.height:
                if self.row + dice_number <= self.height:
                    print(f"{(self.row + dice_number, self.col)}")
            
        
            if self.row + dice_number > self.width and self.grid[self.col][self.row+1] != "⬛️":
                
                difference = (dice_number + self.row) - self.width
                
                self.row = 12
                self.col_right = self.col + difference
                self.col_left = self.col - difference
                
                if self.width > self.col_right > 0:
                    print(f"{(self.row, self.col_right)}") # possibilité à droite
                    
                if self.col_left > 0:
                    print(f"{(self.row, self.col_left)}") # possibilité à gauche
                
            
    
    
    
    def show_title(self):
                return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       TRIVIA PURSUIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━""" 

    
    def show_score(self):
    
        categ = ["🟩","🟪","🟨","🟥","🟦"]
        score = ["⬛️","⬛️","⬛️","⬛️","⬛️"]
        return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   CLASSEMENT DES JOUEURS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
      Score Player #1
        {(''.join(score[:5]))}
      Score Player #2 
        {(''.join(score[:5]))}
      Score Player #3
        {(''.join(score[:5]))}
    """ 

        
    def modify_score():

        # Si le joueur répond correctement à une question d'une catégorie,
        # alors on score.pop()
        # et on score.append(categ[x])
        # on peut aussi ajuster la liste à chaque fois qu'un joueur passe devant un autre joueur
        # afficher la liste des scores de manière croissante/décroissante
        pass
        
            
boardgame = Board(12,12) #taille maximale pour le moment, il faut optimiser la taille dans la méthode de la classe Grid
title = boardgame.show_title()
print(title)
boardgame.create_boardgame()
score_result = boardgame.show_score()
print(score_result)
boardgame.show_available_cells()