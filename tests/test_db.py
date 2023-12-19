import os
import sys
import inspect

# je recherche dans un premier temps le chemin de mon répertoire courant
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# A partir de celui-ci je déduis le chemin de mon répertoire parent
parentdir = os.path.dirname(currentdir)

# J'ajoute le chemin de mon répertoire parent au "python path" 
# qui est l'endroit ou la fonction import va chercher ce qu'elle est capable d'importer
sys.path.insert(0, parentdir) 

from src.db import read_table

def test_all_db():

    categories = ["python", "sql", "git", "terminal", "actu_ia", "soft_skills"]
    ids_used = []

    for category in categories:

        while True:

            question = read_table(category, ids_used)

            if question is None:
                break

            ids_used.append(question["id"])
            print(question)

    print("Nombre de questions posées : ", len(ids_used))
    print("listes des ids : ", ids_used)


def test_one_question(category):
    
    question = read_table(category, [])
    print(question)


test_one_question("python")