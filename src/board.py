class Grid():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        

    def create_boardgame(self):

        # création des lignes (avec des nombres de 1 à 11)
        row = [str(i+1) for i in range(0, self.width+1)]


        # création de la grille (ajout de colonnes)
        # Remove unnecessary string manipulation
        grid = [list(row) for j in range(0, self.height+1)]


        # ajouter valeurs 0 "False" sur lesquelles on ne peut pas jouer
        for i in range(1,10): # ce range = columns
            for index in range(1,5):
                grid[i][index] = "0"
            for index in range(6, 10):
                grid[i][index] = "0"

        # dictionnaire des catégories, première lettre de chaque categ (il faudra leur attribuer des couleurs)
        categories = {1: "P", 2: "S", 3: "G", 4: "T", 5: "A", 6: "M", 7: "A", 8: "T", 9: "G", 10: "S", 11: "P"}

        for row in grid:
            for index in range(len(row)):
                if row[index] in categories:
                    row[index] = categories[row[index]]


        for row_index in range(1, len(grid) - 1):
            grid[row_index][0] = str(row_index + 1)
            grid[row_index][-1] = str(row_index + 1)
            grid[row_index][5] = str(row_index + 1)


        #modifier la ligne du milieu de la grille
        grid[5] = grid[0]

        for row_index in range(len(grid)):
            for col_index in range(len(grid[row_index])):
                if grid[row_index][col_index] == "1" or grid[row_index][col_index] == "11":
                    grid[row_index][col_index] = '🟩'
                elif grid[row_index][col_index] == "2" or grid[row_index][col_index] == "10":
                    grid[row_index][col_index] = '🟪'
                elif grid[row_index][col_index] == "3" or grid[row_index][col_index] == "9":
                    grid[row_index][col_index] = '🟨'
                elif grid[row_index][col_index] == "4" or grid[row_index][col_index] == "8":
                    grid[row_index][col_index] = '🟥'
                elif grid[row_index][col_index] == "5" or grid[row_index][col_index] == "7":
                    grid[row_index][col_index] = '🟦'
                elif grid[row_index][col_index] == "6":
                    grid[row_index][col_index] = '⬜️'
                elif grid[row_index][col_index] == "0":
                    grid[row_index][col_index] = '⬛️'

        # Print the modified grid
        for row in grid:
            #print(row)
            print("".join(row))
        

