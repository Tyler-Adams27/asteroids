import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from ui import *
from death import *


def main():
    pygame.init()
    pygame.display.set_caption('Asteroids')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
 
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                death_ui(pygame.font.Font(None, 36), screen)
                sys,exit()
                
            for shot in shots:
                if asteroid.collides_with(shot):
                    add_to_score(score)
                    shot.kill()
                    asteroid.split()

        screen.fill("black")
        update_ui(score, pygame.font.Font(None, 36), screen)


        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()


        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
