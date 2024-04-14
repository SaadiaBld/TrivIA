from src.board import Board
from src.game import Game
from src.player import Player

if __name__ == "__main__":
	print("")

	# Initialisation du jeu et des objets board, game et players
	nb_player = "0"
	while nb_player != "1" and nb_player != "2" and nb_player != "3" and nb_player != "4" and nb_player != "5":
		nb_player = input("Nombre de joueur : (max 5) ")

	boardgame = Board(12,12)
	
	game = Game(int(nb_player), boardgame)

	game.print_players()
	print("")
	player_turn = 0
	# Affiche la grille
	boardgame.create_boardgame()
	print("")

while game.game_continue():

	# Affichage des possibilités de déplacement, déplacement joueur et affichage grille
	current_player = game.players[game.actual_player]
	current_player.move()

	# Pose une question au joueur
	game.ask_question(current_player)

	current_player.show_score()
	# Affichage et mise à jour du score

	for row in boardgame.grid:
		print("".join(row))

	print("")

	# Joueur suivant
	game.next_player()
