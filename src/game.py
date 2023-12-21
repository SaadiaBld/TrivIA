import random
from src.joueur import Player
from src.db import read_table

# Add jeremy
import networkx as nx

class Game:
    def __init__(self, numbers_of_players, boardgame):
        self.boardgame = boardgame
        self.numbers_of_players = numbers_of_players
        self.players = [Player(i, self.boardgame) for i in range(numbers_of_players)]   
        self.categories = ["⬛️","🟩","🟪","🟨","🟥","🟦", "🟧"]
        self.perfect_score = ["🟩","🟪","🟨","🟥","🟦", "🟧"]
        self.actual_player = 0
        self.ids = []
        self.game_over = False

    def next_player(self):
        self.actual_player += 1
        self.actual_player = self.actual_player % self.numbers_of_players


    def game_continue(self):
        if self.game_over == True:
            return False
        for num_player in range(self.numbers_of_players):
            if (self.players[num_player].score == self.perfect_score):
                print("Bravo, " + self.players[num_player].token  + " gagne la partie !")
                return False
        return True

    def print_players(self):
        for player in self.players:
            print(player.name + " " + player.token)


    # def print_score(self):
    #     for player in self.players:
    #         affichage = ""
    #         for score in player.score:
    #             affichage += self.categories[score]
    #         print ("le score de " + player.token + " " + affichage)


    def roll_dice(self):
        # tirer au sort un nombre entre 1 et 6
        dice_number = random.choice(range(1,7))
        return dice_number
        # dé 3D? comment animer un .obj en python?
        # dé 3D? animations Blender
        # images des faces d'un dé?

    
    def ask_question(self, player):

        self.categories = {
        "🟩" : "python",
        "🟪" : "sql",
        "🟨" : "git",
        "🟥" : "terminal",
        "🟦" : "actu_ia",
        "🟧" : "soft_skills"}

        # categories["1"][0]

        # retourne la catégorie de la case sur laquelle le joueur se trouve



        categ = self.categories[player.color_of_question]

        dictionnaire_avec_question = read_table(categ, self.ids)

        if dictionnaire_avec_question is None:
            self.game_over = True
            return

        # print(dictionnaire_avec_question)
        self.ids.append(dictionnaire_avec_question["id"])

        # afficher la question (sortie de manière aléatoire via SQL)
        print("QUESTION: " + dictionnaire_avec_question["question"])

        # randomiser et afficher les réponses (pour éviter que ce soit toujours la réponse A la réponse correcte)
        i = 0
        for j in random.sample(["correct_answer", "incorrect_answer_1", "incorrect_answer_2", "incorrect_answer_3"], 4):
                i+=1
                print(f"{i}. {dictionnaire_avec_question[j]}")
                
                if j == "correct_answer":
                    self.correct_number = i

        # demander de choisir une réponse à l'utilisateur
        print("")
        self.user_answer = input("Merci de taper le chiffre correspondant à la réponse que vous souhaitez donner : ")

        if int(self.user_answer) == self.correct_number:

            print("Bravo! Bonne réponse")

            for i in range(len(player.score)):
                if self.perfect_score[i] == player.color_of_question:
                    player.score[i] = 1#self.perfect_score[i]
                    #print(self.perfect_score[i])
                    #print(player.score)

            # if self.categories[str(self.col)][1] not in self.score:
            #     self.score = self.score.pop()
            #     self.score = self.score.append(self.categories[str(self.col)][1])
            # else:
            #     pass

        else:

            print("Raté.")
            print("La bonne réponse etait : " + dictionnaire_avec_question["correct_answer"])




    def create_graph(self):
        # Créer un graphe vide
        G = nx.Graph()

        n_ext = 48
        n_total = 69

        # Création du cercle extérieur
        for i in range(0, n_ext):
            G.add_node(i)

        # Création des arrêtes extérieurs
        for i in range(0, n_ext-1):
            G.add_edge(i, i + 1)

        # La boucle est bouclée
        G.add_edge(n_ext-1, 0)

        # Création des chemins intérieurs
        for i in range(n_ext, n_total):
            G.add_node(i)

        centre = 53

        # Branche 1
        for i in range(48, 58):
            G.add_edge(i, i + 1)

        # Branche 2
        for i in range(59, 64):
            G.add_edge(i, i + 1)

        # Branche 2 bis
        for i in range(64, 69):
            G.add_edge(i, i + 1)

        # Connexions spéciales à l'extérieur
        G.add_edge(6, 59)
        G.add_edge(18, 58)
        G.add_edge(30, 68)
        G.add_edge(42, 48)

        # Connexions spéciales à l'intérieur
        G.add_edge(centre, 63)
        G.add_edge(centre, 64)

        return G