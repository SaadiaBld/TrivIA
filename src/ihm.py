import pygame
import math

class Ihm:
    def __init__(self, largeur, hauteur):
        pygame.init()
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Trivial Pursuit")

    def dessiner_plateau(self):
        # Les couleurs représentant différentes sections
        couleurs = [
            (255, 0, 0),    # Rouge
            (255, 255, 0),  # Jaune
            (0, 255, 0),    # Vert
            (0, 0, 255),    # Bleu
            (255, 0, 255),  # Magenta
            (0, 255, 255)   # Cyan
        ]


        nb_sections = len(couleurs)
        rayon = 100
        centre = (self.largeur // 2, self.hauteur // 2)

        angle = 360 / nb_sections

        for i in range(nb_sections):
            start_angle = math.radians(i * angle)
            end_angle = math.radians((i + 1) * angle)
            pygame.draw.circle(self.fenetre, couleurs[i], centre, rayon)
            # Mettre en place des lignes pour séparer les sections (facultatif)
            x = centre[0] + int(rayon * math.cos(end_angle))
            y = centre[1] + int(rayon * math.sin(end_angle))
            pygame.draw.line(self.fenetre, (0, 0, 0), centre, (x, y), 3)

 #   def dessin_test(self):
  #  	screen[3] = 8
   # 	print screen()


    def afficher(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.fenetre.fill((255, 255, 255))  # Fond blanc
            self.dessiner_plateau()
            self.dessin_test()
            pygame.display.update()