import pygame
from main import *
# test
score = 0

def update_ui(score,font,screen):
    score_text = font.render(f"{score}", True, "White")
    screen.blit(score_text, (10, 10))


def add_to_score(score):
    score += 1
    return score


