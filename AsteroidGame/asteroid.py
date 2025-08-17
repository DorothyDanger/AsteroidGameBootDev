import circleshape
import pygame
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_SPAWN_RATE
import random
class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        pygame.draw.circle(screen, color="gray", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        # Small asteroids are not split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Random angle, splitting in opposite directions
        random_angle = random.uniform(20,50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vector1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = vector2
        