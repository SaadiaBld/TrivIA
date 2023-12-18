import pandas as pd
import sqlite3


def get_database(func):
    """Decorateur qui initialise la connexion avec la bdd, lance une action sur la bdd puis ferme la connexion"""

    def wrap(*args, **kargs):
        con = sqlite3.connect("trivia.db")
        cur = con.cursor()
        result = func(*args, *kargs, cur)
        con.commit()
        con.close()
        return result
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
    data = pd.read_csv("questions_trivia.csv")
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
    """
    Requete la table questions pour obtenir une ligne de question pas encore obtenue sur un thème spécifique.
    category = str | ids_used = list of int
    """
    
    if len(ids_used) == 0:
        query = "SELECT * FROM Questions WHERE category = ? ORDER BY Random() LIMIT 1"
        args = (category,)
    
    else:
        qm = ", ".join("?" * len(ids_used)) # Crée le nombre de ? nécessaires correspondant au nombre d'id déjà utilisés
        query = f"SELECT * FROM Questions WHERE category = ? AND id NOT IN ({qm}) ORDER BY Random() LIMIT 1"
        args = (category, *ids_used)

    cur.execute(query, args)
    result = cur.fetchall()
    question = {
        'id': result[0][0],
        'category': result[0][1],
        'difficulty': result[0][2],
        'question': result[0][3],
        'correct_answer': result[0][4],
        'incorrect_answer_1': result[0][5],
        'incorrect_answer_2': result[0][6],
        'incorrect_answer_3': result[0][7],
    }
    return question

    
@get_database
def delete_table(cur):
    """Supprime la table question"""

    cur.execute("""DROP TABLE Questions""")