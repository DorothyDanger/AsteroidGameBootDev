import pygame
#import constants
from constants import *
from player import Player
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    displayWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    while True:
        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS
        player.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(displayWindow, color="black") # Fill the screen with black
        player.draw(displayWindow)
        pygame.display.flip()
    
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
