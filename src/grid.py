import random
import pandas as pd
from src.db import read_table
from src.joueur import *

class Board:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.col = int(width/2)
		self.row_middle = int(height/2)  #renommé self.row en self.row_middle pr eviter conflits avec self.row
		self.user_answer = 0
		self.correct_answer = 0
		self.score = []
		self.dico_score = {}
        # self.numbers_of_players = numbers_of_players
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
		# for i in range(1, 12):
		# 	grid[i][i] = categories[str(i+1)][1]
		# 	grid[i][self.width - i] = categories[str(self.width - i + 1)][1]
            
                
        # Modification du centre de la grille    #START
		grid[6][6] = categories["14"][1]
        
        
        # test d'affichage
		old_value = grid[7][12]
        #grid[7][12] = "X"
		old_value


        # Affichage de la grille 
		for row in grid:
			print("".join(row))
                 
