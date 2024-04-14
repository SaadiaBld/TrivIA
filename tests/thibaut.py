import random

class Board():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        
    def create_boardgame(self):

        # Création des lignes (avec des nombres de 1 à 11)
        row = [str(i+1) for i in range(0, self.width+1)]

        # Création de la grille (ajout de colonnes)
        grid = [list(row) for j in range(0, self.height+1)]

        # Ajout de valeurs 0 "False" sur lesquelles on ne peut pas jouer
        for i in range(1,12): # ce range = columns
            for index in range(1,6):
                grid[i][index] = "0"
            for index in range(7, 12):
                grid[i][index] = "0"


        # Dictionnaire des catégories avec leurs couleurs correspondantes
        categories = {"0": [0, "⬛️"],
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
        #imaginons que sa position soit celle de START
        
        # start_position = grid[5][5]
        # player_position = start_position
        
        # for i in range(1,7):
        #     if i == dice_number:
        #         available_cells = player_position[i][i]
        #         available_cells
        
        pass
    
    
    def show_available_cells():
        # illuminer uniquement les cases où le joueur peut se déplacer
        # calculer la position de ces cases en fonction de la position du joueur
        pass
    
    
    def show_title(self):
                return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━
       TRIVIA PURSUIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━""" 

    
    def show_score(self):
    
        categ = ["🟩","🟪","🟨","🟥","🟦"]
        score = ["⬛️","⬛️","⬛️","⬛️","⬛️"]
        return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━
   CLASSEMENT DES JOUEURS
━━━━━━━━━━━━━━━━━━━━━━━━━━━
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