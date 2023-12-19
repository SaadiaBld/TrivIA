from src.board import Board
from src.game import Game
from src.ihm import Ihm

#grille = Grid(10,10) #taille maximale pour le moment, il faut optimiser la taille dans la méthode de la classe Grid
#grille.create_boardgame()


# Création de l'interface utilisateur avec une fenêtre de 800x600
#if __name__ == "__main__":
#    interface = Ihm(800, 600)
#    interface.afficher()


#boardgame = Board(12,12) #taille maximale pour le moment, il faut optimiser la taille dans la méthode de la classe Grid
#title = boardgame.show_title()
#print(title)
#boardgame.create_boardgame()
#score_result = boardgame.show_score()
#print(score_result)
#boardgame.show_available_cells()


if __name__ == "__main__":
	game = Game(2)
	game.print_players()
	boardgame = Board(12,12)
	title = boardgame.show_title()
	print(title)
	boardgame.create_boardgame()
	boardgame.show_available_cells()


while game.game_continue():
	game.players[1].score += 1
	game.print_score()
	score_result = boardgame.show_score()
	print(score_result)




