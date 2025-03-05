import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
import sys
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    dt = 0
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots,updatable,drawable)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        for i in asteroids:
            if player.collide(i):
                print("Game Over!")
                sys.exit(0)
        for shot in shots:
            shot.draw(screen)

        screen.fill("Black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()