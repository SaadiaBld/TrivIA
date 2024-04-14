import random
from src.player import Player
from src.db import read_table

class Game:
    def __init__(self, numbers_of_players, boardgame):
        self.boardgame = boardgame
        self.numbers_of_players = numbers_of_players
        self.players = [Player(i, self.boardgame) for i in range(numbers_of_players)]   
        self.categories = ["⬛️","🟩","🟪","🟨","🟥","🟦", "🟧"]
        self.perfect_score = [1, 1, 1, 1, 1, 1]#["🟩","🟪","🟨","🟥","🟦", "🟧"]
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
            #print(f"{self.players[num_player].token} : {self.players[num_player].score }  - {self.perfect_score}")
            if (self.players[num_player].score == self.perfect_score):
                print("Bravo, " + self.players[num_player].token  + " gagne la partie !")
                return False
        return True

    def print_players(self):
        for player in self.players:
            print(player.name + " " + player.token)

    def ask_question(self, player):

        self.categories = {
        "🟩" : "python",
        "🟪" : "sql",
        "🟨" : "git",
        "🟥" : "terminal",
        "🟦" : "actu_ia",
        "🟧" : "soft_skills"}

        # retourne la catégorie de la case sur laquelle le joueur se trouve
        categ = self.categories[player.color_of_question]

        dictionnaire_avec_question = read_table(categ, self.ids)

        if dictionnaire_avec_question is None:
            print("Game Over. Personne ne gagne.")
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
        available_answer = ['1', '2', '3', '4']
        while self.user_answer not in available_answer:
            self.user_answer = input("Merci de taper le chiffre correspondant à la réponse que vous souhaitez donner : ")

        if int(self.user_answer) == self.correct_number:

            print("Bravo! Bonne réponse")

            for i in range(len(player.score)):
                perfect_score = ["🟩","🟪","🟨","🟥","🟦", "🟧"]
                if perfect_score[i] == player.color_of_question:
                    player.score[i] = 1
        else:
            print("Raté.")
            print("La bonne réponse etait : " + dictionnaire_avec_question["correct_answer"])