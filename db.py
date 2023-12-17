import pandas as pd
import sqlite3


def get_database(func):
    """Decorateur qui initialise la connexion avec la bdd, lance une action sur la bdd puis ferme la connexion"""

    def wrap(*args, **kargs):
        con = sqlite3.connect("trivIA.db")
        cur = con.cursor()
        func(*args, *kargs, cur)
        con.commit()
        con.close()
    return wrap


@get_database
def create_table(cur):
    """Crée la table questions dans la bdd"""

    cur.execute("""
                CREATE TABLE IF NOT EXISTS Questions (
                id integer PRIMARY KEY, 
                category varchar(255), 
                difficulty varchar(255), 
                question text, 
                correct_answer varchar(255), 
                incorrect_answer_1 varchar(255), 
                incorrect_answer_2 varchar(255), 
                incorrect_answer_3 varchar(255))
                """
    )


@get_database
def update_table(cur):
    """Met à jour la table questions à partir d'un fichier csv"""

    # Charge le csv dans un dataframe
    data = pd.read_csv("questions.csv")
    df = pd.DataFrame(data)
    for row in df.itertuples():

        # Vérifie si la question existe déjà dans la table
        cur.execute("""SELECT question FROM Questions WHERE question = ?""", (row.question,))
        result = cur.fetchall()
        if result:
            continue
        
        # Sinon rajoute la question
        cur.execute("""
                    INSERT INTO 
                    Questions (category, difficulty, question, correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (row.category, row.difficulty, row.question, row.correct_answer, row.incorrect_answer_1, row.incorrect_answer_2, row.incorrect_answer_3)
        )


@get_database
def read_table(category, ids_used, cur):
    """Requete la table questions pour obtenir une ligne de question pas encore obtenue sur un thème spécifique"""

    # A DECIDER -> Deux options pour gérer les questions à afficher en jeux : 

    # 1 - On crée un objet qui va contenir toutes les questions, puis on cherche dans l'objet
        # cur.execute("""SELECT * FROM Questions""")
        # result = cur.fetchall()

    # 2 - On requete la table pour obtenir une question sur une catégorie dans un ordre aléatoire 

    query = "SELECT * FROM Questions WHERE category = ? AND id NOT IN (%s)" % ",".join("?" for i in ids_used) + (" ORDER BY Random() LIMIT 1")
    cur.execute(query, ids_used)
    result = cur.fetchall()
    question = {
        'category': result[1],
        'difficulty': result[2],
        'question': result[3],
        'correct_answer': result[4],
        'incorrect_answer_1': result[5],
        'incorrect_answer_2': result[6],
        'incorrect_answer_3': result[7],
    }
    print(question)

    
@get_database
def delete_table(cur):
    """Supprime la table question"""

    cur.execute("""DROP TABLE Questions""")


def main():
    print("en cours")
    read_table("Moyenne", [26, 27])

if __name__ == '__main__':
    main()