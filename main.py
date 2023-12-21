from src.grid import Board
from src.game import Game
from src.ihm import Ihm
from src.joueur import Player

#grille = Grid(10,10) #taille maximale pour le moment, il faut optimiser la taille dans la méthode de la classe Grid
#grille.create_boardgame()

# Création de l'interface utilisateur avec une fenêtre de 800x600
# if __name__ == "__main__":
#     interface = Ihm(1100, 800)
#     interface.afficher_board()

if __name__ == "__main__":

	# Initialisation du jeu et des objets board, game et players
	nb_player = "0"
	while nb_player != "1" and nb_player != "2" and nb_player != "3" and nb_player != "4" and nb_player != "5":
		nb_player = input("Nombre de joueur : (max 5) ")

	boardgame = Board(12,12)
	# title = boardgame.show_title()
	# print(title)

	
	game = Game(int(nb_player), boardgame)

	game.print_players()
	player_turn = 0
	boardgame.create_boardgame()
	G = game.create_graph()
	



while game.game_continue():

	# Affiche la grille
	# print(title)

	# Affiche le score des joueurs
	# game.print_score()

	# Lance un dé pour sélectionner les cases disponibles pour le déplacement
	dice = game.roll_dice()
	# boardgame.show_available_cells()

	# Affichage des possibilités de déplacement, déplacement joueur et affichage grille
	current_player = game.players[game.actual_player]
	current_player.move(G, dice, 53)

	# Pose une question au joueur
	# boardgame.ask_question()
	game.ask_question(current_player)

	current_player.show_score()
	# Affichage et mise à jour du score
	# game.print_score()

	# Joueur suivant
	# game.next_player()
	for row in boardgame.grid:
		print("".join(row))
	input ("")

	print("")

	game.next_player()
