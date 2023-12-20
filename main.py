from src.board import Board
from src.game import Game
#from src.ihm import Ihm

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
	nb_player = "0"
	while nb_player != "1" and nb_player != "2" and nb_player != "3" and nb_player != "4" and nb_player != "5":
		nb_player = input("Nombre de joueur : (max 5) ")
	game = Game(int(nb_player))
	game.print_players()
	boardgame = Board(12,12)
	title = boardgame.show_title()
	print(title)
	boardgame.create_boardgame()
	#boardgame.show_available_cells()

tmp = 0
while game.game_continue():
	game.players[1].score[tmp]=tmp+1
	tmp += 1
	game.print_score()

	input ("Roll the dice !")

	# lance de 
	dice = game.roll_dice()

	#affichage map avec possibilite de deplacement
	boardgame.show_available_cells(dice)

	# choix deplacement (input 1,2,3,4) choose_move

	# affichage map ?

	# question. (input reponse 1,2,3,4)
	# boardgame.ask_question()
	# resultat de reponse (update score) et affichage score



	print("")



