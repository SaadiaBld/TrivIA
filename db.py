import sqlite3
import csv

def create_database():

    db = sqlite3.connect("trivIA")

""""
CREATE TABLE Questions (
id primary key,
theme varchar(255),
difficulty varchar(255),
question text,
correct_answer varchar(255),
incorrect_answer_1 varchar(255),
incorrect_answer_2 varchar(255),
incorrect_answer_3 varchar(255),
);
"""