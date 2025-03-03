import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player(x,y,PLAYER_RADIUS)
    player = Player(x,y,PLAYER_RADIUS)
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 100000000

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="Black")
        player.update(dt)
        player.draw(screen=screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000






if __name__ == "__main__":
    main()