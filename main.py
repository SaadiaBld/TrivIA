from src.board import Grid
from src.game import Game
from src.ihm import Ihm

#grille = Grid(10,10) #taille maximale pour le moment, il faut optimiser la taille dans la méthode de la classe Grid
#grille.create_boardgame()


# Création de l'interface utilisateur avec une fenêtre de 800x600
#if __name__ == "__main__":
#    interface = Ihm(800, 600)
#    interface.afficher()


if __name__ == "__main__":
	game = Game(4)
	game.print_players()

