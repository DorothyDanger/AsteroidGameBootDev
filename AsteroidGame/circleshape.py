import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    # Check for collision. If the distance between the centers of two circles is less than or equal to the sum of their radii, they are colliding.
    # This is used to check if the player collides with an asteroid.
    def collission(self, other):
        return self.position.distance_to(other.position) <= (self.radius + other.radius)