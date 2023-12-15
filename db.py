import sqlite3
import csv

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
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Questions (id int PRIMARY KEY, category varchar(255), difficulty varchar(255), question text, correct_answer varchar(255), incorrect_answer_1 varchar(255), incorrect_answer_2 varchar(255), incorrect_answer_3 varchar(255))"
    )

@get_database
def update_table(cur):
    with open("questions.csv", "r") as file:
        reader = csv.reader(file)
    

@get_database
def delete_table(cur):
    cur