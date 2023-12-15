import pandas as pd
import sqlite3

def get_database(func):

    def wrap():

        con = sqlite3.connect("trivIA.db")
        cur = con.cursor()
        func(cur)
        con.commit()
        con.close()
        return wrap


@get_database
def create_table(cur):

    cur.execute("""
                CREATE TABLE IF NOT EXISTS Questions (
                id int PRIMARY KEY, 
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

    data = pd.read_csv("questions.csv")
    df = pd.DataFrame(df)
    for row in df.itertuples():
        cur.execute("""
                    INSERT INTO 
                    Questions (category, difficulty, question, correct_answer, incorrect_answer_1, incorrect_answer_2, incorrect_answer_3)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    row.category, row.difficulty, row.question, row.correct_answer, row.incorrect_answer_2, row.incorrect_answer_3
        )

    

@get_database
def delete_table(cur):
    pass

def __init__():
    create_table()
    update_table()
    print("done")
