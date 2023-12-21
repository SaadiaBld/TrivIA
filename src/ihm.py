import pygame
import math

class Ihm:
    def __init__(self, largeur, hauteur):
        pygame.init()
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        self.pos = {}
        pygame.display.set_caption("Fenêtre Pygame")
        self.pos_player = 26
        self.size_cercle = 19

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

    def afficher_board(self):
        running = True



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

                pygame.draw.circle(self.fenetre, color, (x, y), self.size_cercle)

                self.pos[i] = (x, y)

                if angle == 0:
                    for c in range(6):
                        xp = x - 46 * c - 46
                        self.pos[100+c] = (xp, y)
                        pygame.draw.circle(self.fenetre, self.color_choice(c+4), (xp, y), self.size_cercle)
                elif angle == 60:
                    for c in range(6):
                        xp = x - 23 * c - 23
                        yp = y - 40 * c - 40
                        self.pos[200+c] = (xp, yp)
                        pygame.draw.circle(self.fenetre, self.color_choice(c+5), (xp, yp), self.size_cercle)
                elif angle == 120:
                    for c in range(6):
                        xp = x + 23 * c + 23
                        yp = y - 40 * c - 40
                        self.pos[300+c] = (xp, yp)
                        pygame.draw.circle(self.fenetre, self.color_choice(c), (xp, yp), self.size_cercle)
                elif angle == 180:
                    for c in range(6):
                        xp = x + 46 * c + 46
                        self.pos[400+c] = (xp, y)
                        pygame.draw.circle(self.fenetre, self.color_choice(c+1), (xp, y), self.size_cercle)
                elif angle == 240:
                    for c in range(6):
                        xp = x + 23 * c + 23
                        yp = y + 40 * c + 40
                        self.pos[500+c] = (xp, yp)
                        pygame.draw.circle(self.fenetre, self.color_choice(c+2), (xp, yp), self.size_cercle)
                elif angle == 300:
                    for c in range(6):
                        xp = x - 23 * c - 23
                        yp = y + 40 * c + 40
                        self.pos[600+c] = (xp, yp)
                        pygame.draw.circle(self.fenetre, self.color_choice(c+3), (xp, yp), self.size_cercle)
                
            self.player()

            #centre TODO. marche po
            pygame.draw.circle(self.fenetre, (255, 255, 255), (centre_x, centre_y), self.size_cercle)


            # pygame.display.flip()  # Met à jour l'affichage
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

    def move_player(self, new_pos):
        self.pos_player = new_pos
        pygame.draw.circle(self.fenetre, (255, 255, 255), (self.pos[self.pos_player][0], self.pos[self.pos_player][1]), 5)
        pygame.display.flip()



    def player(self):
        if (self.pos_player == 43):
            self.pos_player = 0
        if(self.pos_player == -1):
            self.pos_player = 42

        # print(self.pos_player)

        #print ("pos joueur: " + str(self.pos[self.pos_player][0]) + ", " + str(self.pos[self.pos_player][1]))

        # print(str(self.pos_player) + " : (" + str(self.pos[self.pos_player%42][0]) + ", " + str(self.pos[self.pos_player%42][1]) + ")")


        for event in pygame.event.get():
            #met a jour l'affichage
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Si un clic de souris est détecté
                if event.button == 1:  # Vérifie si c'est le bouton gauche de la souris
                    mouse_x, mouse_y = pygame.mouse.get_pos()  # Récupère la position de la souris
                    for key, value in self.pos.items():
                        x, y = value
                        distance = math.sqrt((mouse_x - x) ** 2 + (mouse_y - y) ** 2)
                        if distance < self.size_cercle:  # Si la souris est à l'intérieur du cercle
                            print(f"Clic sur le cercle {key} à la position ({x}, {y}) avec la couleur {self.color_choice(key)}")
                            self.move_player(key)
                            break  # Sort de la boucle dès qu'un cercle est cliqué
            elif event.type == pygame.KEYDOWN:  # Vérifie si une touche est enfoncée
                if event.key == pygame.K_ESCAPE:  # Flèche de droite
                    print("Fin du jeu")
                    running = False
                    pygame.quit()
                # TODO : crash plus que ca quitte le jeu, a revoir !
                pygame.display.flip()


        # for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             running = False
        #         elif event.type == pygame.KEYDOWN:  # Vérifie si une touche est enfoncée
        #             if event.key == pygame.K_UP:  # Flèche du haut
        #                 print("La touche UP a été enfoncée.")
        #                 self.pos_player -= 1
        #             elif event.key == pygame.K_DOWN:  # Flèche du bas
        #                 print("La touche DOWN a été enfoncée.")
        #                 self.pos_player += 1
        #             elif event.key == pygame.K_LEFT:  # Flèche de gauche
        #                 if (self.pos_player == 0):
        #                     self.pos_player = 100
        #                 elif (self.pos_player == 8):
        #                     self.pos_player = 200
        #                 elif(self.pos_player == 15):
        #                     self.pos_player = 300
        #                     print("La touche LEFT a été enfoncée.")
        #             elif event.key == pygame.K_RIGHT:  # Flèche de droite
        #                 print("La touche RIGHT a été enfoncée.")
        #             elif event.key == pygame.K_ESCAPE:  # Flèche de droite
        #                 print("Fin du jeu")
        #                 pygame.quit()
        #                 # TODO : crash plus que ca quitte le jeu, a revoir !


    