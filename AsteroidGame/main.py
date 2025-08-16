import pygame
#import constants
from constants import *
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    displayWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(displayWindow, color="black") # Fill the screen with black
        pygame.display.flip()
    
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
