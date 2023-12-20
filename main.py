from src.board import Board
#from src.game import Game
from src.ihm import Ihm

#grille = Grid(10,10) #taille maximale pour le moment, il faut optimiser la taille dans la méthode de la classe Grid
#grille.create_boardgame()

# Création de l'interface utilisateur avec une fenêtre de 800x600
if __name__ == "__main__":
    interface = Ihm(1100, 800)
    interface.afficher_board()

# if __name__ == "__main__":

# 	# Initialisation du jeu et des objets board, game et players

# 	boardgame = Board(12,12)
# 	title = boardgame.show_title()
# 	print(title)

# 	nb_player = "0"
# 	while nb_player != "1" and nb_player != "2" and nb_player != "3" and nb_player != "4" and nb_player != "5":
# 		nb_player = input("Nombre de joueur : (max 5) ")
# 	game = Game(int(nb_player), boardgame)

# 	game.print_players()
# 	player_turn = 0


# while game.game_continue():

# 	# Affiche la grille
# 	print(title)
# 	boardgame.create_boardgame()

# 	# Affiche le score des joueurs
# 	game.print_score()

<<<<<<< HEAD
	# Lance un dé pour sélectionner les cases disponibles pour le déplacement
	dice = game.roll_dice()
	boardgame.show_available_cells()

	# Affichage des possibilités de déplacement, déplacement joueur et affichage grille
	boardgame.choose_move()
=======
# 	# Lance un dé pour sélectionner les cases disponibles pour le déplacement
# 	#dice = game.roll_dice()
# 	boardgame.show_available_cells()

# 	# Affichage des possibilités de déplacement, déplacement joueur et affichage grille
>>>>>>> 44f84049004e11edbd861164bdff3da5021c43b3

# 	# Pose une question au joueur
# 	boardgame.ask_question()

# 	# Affichage et mise à jour du score
# 	game.print_score()

<<<<<<< HEAD
	# Joueur suivant
	game.next_player()

=======
# 	# Joueur suivant
# 	game.next_player()
>>>>>>> 44f84049004e11edbd861164bdff3da5021c43b3
