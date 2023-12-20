import pygame
import math

class Ihm:
    def __init__(self, largeur, hauteur):
        pygame.init()
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Fenêtre Pygame")

    def color_choice(self, i):
        blue = (0, 0, 255)
        red = (255, 0, 0)
        green = (0, 255, 0)
        purple = (142, 68, 173)
        yellow = (247, 220, 111)
        orange = (211, 84, 0)

        if (i % 6 == 0):
            color = red
        elif (i % 6 == 1):
            color = blue
        elif (i % 6 == 2):
            color = orange
        elif (i % 6 == 3):
            color = yellow
        elif (i % 6 == 4):
            color = purple
        elif (i % 6 == 5):
            color = green
        return color

    def afficher(self):
        running = True


        size_cercle = 19

        while running:
            self.fenetre.fill((0, 0, 0))  # Remplit la fenêtre avec du noir
            
            # Dessiner 30 ronds colorés de rayon 30 pixels en cercle
            centre_x, centre_y = self.largeur // 2, self.hauteur // 2  # Centre de la fenêtre
            rayon_cercle = 320  # Rayon du cercle
            
            centre_x -= 30
            centre_y -= 30

            for i in range(42):
                angle = i * (360 / 42)  # Angle pour chaque rond
                x = centre_x + int(rayon_cercle * math.cos(math.radians(angle))) # Calcul de la position x
                y = centre_y + int(rayon_cercle * math.sin(math.radians(angle)))  # Calcul de la position y
                
                # Dessin du rond
                color = self.color_choice(i)

                pygame.draw.circle(self.fenetre, color, (x, y), size_cercle)

                if angle == 0:
                    for c in range(6):
                        pygame.draw.circle(self.fenetre, self.color_choice(c), (x - 46 * c - 46, y), size_cercle)





            pygame.draw.circle(self.fenetre, (255, 255, 255), (centre_x, centre_y), size_cercle)


            # pygame.draw.circle(self.fenetre, purple, (centre_x, centre_y + 80), size_cercle)
            # pygame.draw.circle(self.fenetre, yellow, (centre_x, centre_y + 160), size_cercle)
            # pygame.draw.circle(self.fenetre, orange, (centre_x, centre_y + 240), size_cercle)
            # pygame.draw.circle(self.fenetre, purple, (centre_x, centre_y - 80), size_cercle)
            # pygame.draw.circle(self.fenetre, yellow, (centre_x-60, centre_y - 160), size_cercle)
            # pygame.draw.circle(self.fenetre, orange, (centre_x - 120, centre_y - 220), size_cercle)

            # pygame.draw.circle(self.fenetre, red, (centre_x + 80, centre_y), size_cercle)
            # pygame.draw.circle(self.fenetre, green, (centre_x + 160, centre_y), size_cercle)
            # pygame.draw.circle(self.fenetre, blue, (centre_x + 240, centre_y), size_cercle)
            # pygame.draw.circle(self.fenetre, red, (centre_x - 80, centre_y), size_cercle)
            # pygame.draw.circle(self.fenetre, green, (centre_x - 160, centre_y), size_cercle)
            # pygame.draw.circle(self.fenetre, blue, (centre_x - 240, centre_y), size_cercle)


            pygame.display.flip()  # Met à jour l'affichage
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

