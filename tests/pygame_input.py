import inspect
import os
import pygame as pygame
import sys

# je recherche dans un premier temps le chemin de mon répertoire courant
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# A partir de celui-ci je déduis le chemin de mon répertoire parent
parentdir = os.path.dirname(currentdir)

# J'ajoute le chemin de mon répertoire parent au "python path" 
# qui est l'endroit ou la fonction import va chercher ce qu'elle est capable d'importer
sys.path.insert(0, parentdir) 

from src.db import read_table


def tmp_get_question():

    question = read_table("python", [])
    return question


def draw_rectangles(width, height):

    question_width = width
    question_height = height / 2
    answer_width = width / 2
    answer_height = height / 4

    # (x, y, widht, height)
    rect_question = (0, 0, question_width, question_height)
    rect_answers = []
    rect_answers.append((0, question_height, answer_width, answer_height))
    rect_answers.append((answer_width, question_height, answer_width, answer_height))
    rect_answers.append((0, question_height+answer_height, answer_width, answer_height))
    rect_answers.append((answer_width, question_height+answer_height, answer_width, answer_height))
    
    rects = []
    rects.append(pygame.Rect(rect_question))
    for answer in rect_answers:
        rects.append(pygame.Rect(answer))
    return rects


def display_question(width, height):

    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Question affiché")

    white = (255, 255, 255)
    black = (0, 0, 0)

    rects = draw_rectangles(width, height)
    question = tmp_get_question()

    font = pygame.font.Font(None, 24)
    text_surface = font.render(question["question"], True, black)
    text_rect = text_surface.get_rect()

    running = True

    while running:

        window.fill(white)
        for rect in rects:
            pygame.draw.rect(window, white, rect)
            text_rect.center = rect.center
            window.blit(text_surface, text_rect.topleft)

        pygame.display.flip()

tmp_get_question()
display_question(1000, 400)


    # background = (255, 255, 255)

    
        # pygame.draw.rect(window_question, background, rect_question)
        # for answer in rect_answers:
        #     pygame.draw.rect(window_question, background, answer, 2)

        # text = font.render("test", True, (255, 255, 255))
        # text_rect = text.get_rect(center=(answer[0] + answer[2] // 2, answer[1] + answer[3] // 2))
        # window_question.blit(text, text_rect)