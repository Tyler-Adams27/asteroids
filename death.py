import pygame
from constants import *




def death_ui(font,screen):
    death_text = font.render("Game Over", True, "White")
    screen.blit(death_text, (SCREEN_WIDTH / 2.25, SCREEN_HEIGHT / 2))
    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.quit()
    quit()
