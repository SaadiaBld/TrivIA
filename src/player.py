from random import *

class Player:
    #self.position = position
    #position_initiale = 6,6 avec la taille initiale de 11*11

    def __init__(self, id):
        self.id = id
        self.name = input("What's your name?: ")
        self.token = "🦊"
        self.score = [0,0,0,0,0,0]
        self.x = 6
        self.y = 6
    
    def roll_dice(self):
        dice = randint(1, 6)
        return dice
    
    def choose_move(self):
        """On définit ici la logique de déplacement lorsque le joueur est dans les arêtes du milieu"""
        if self.y == 6 and self.x == 6:
            choix1 = self.x + self.roll_dice()
            choix2 = self.x - self.roll_dice()
            choix3 = self.y + self.roll_dice()
            choix4 = self.y - self.roll_dice()

            print("Choisissez votre déplacement: ")
            print(f" 1. Vers la droite : {choix1}")
            print(f" 2. Vers la gauche : {choix2}")
            print(f" 3. Vers le haut: {choix4}")
            print(f" 4. Vers le bas : {choix3}")

            direction_choix = input("Choisissez votre direction:  ")
            if direction_choix == "1":
                self.x = choix1
            elif direction_choix == "2":
                self.x = choix2
            elif direction_choix == "3":
                self.y = choix3
            elif direction_choix == "4":
                self.y = choix4

            return self.y,self.x                
        
        if self.y == 6: #si le joueur est sur la ligne indice 6
            choix1 = self.x + self.roll_dice()
            choix2 = self.x - self.roll_dice()
            position_choix = input("Choisissez votre déplacement: {} or {}".format(choix1,choix2 ))
            self.x = int(position_choix)
            return self.y,self.x
        
        if self.x == 6:
            choix1 = self.y + self.roll_dice()
            choix2 = self.y - self.roll_dice()
            position_choix = input("Choisissez votre déplacement: {} ou  {}".format(choix1,choix2))
            self.y = int(position_choix)
            return self.y, self.x
        

    def answer_question(self):

        pass 
    
    def upgrade_score(self):
        if self.answer_question == correct_answer:
            self.score += 1
        return self.score
    
    def show_score(self):
        return self.upgrade_score