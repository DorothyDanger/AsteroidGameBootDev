import pygame
#import constants
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    # Create sprite groups
    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    # Add objects to the sprite groups
    Asteroid.containers = (update_group, draw_group, asteroid_group)
    Player.containers = (update_group, draw_group)
    AsteroidField.containers = (update_group)

    # Create instances of asteroids and player + display window
    asteroid_field = AsteroidField()
    displayWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    
    

    while True:
        dt = clock.tick(60) / 1000.0  # Limit to 60 FPS
        update_group.update(dt)  # Update all sprites in the group
        for asteroid in asteroid_group:
            if player.collission(asteroid):
                # Handle collision 
                print("Game Over!")
                pygame.quit()
                return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(displayWindow, color="black") # Fill the screen with black
        for sprite in draw_group:
            sprite.draw(displayWindow) # Draw all sprites in the group
        pygame.display.flip()
    
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
