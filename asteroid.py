
import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 5)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # New asteroid spawning
        random_angle = random.uniform(0, 360)
        new_velocity1 = pygame.Vector2(1, 0).rotate(random_angle)
        offset1 = new_velocity1 * 10  # Slide
        new_asteroid1 = Asteroid(self.position.x + offset1.x, self.position.y + offset1.y, new_radius)
        new_asteroid1.velocity = new_velocity1 * 50  # Speed increment

        # Second asteroid spawning
        random_angle2 = random.uniform(0, 360)
        new_velocity2 = pygame.Vector2(1, 0).rotate(-random_angle)
        offset2 = new_velocity2 * 10  # Slide
        new_asteroid2 = Asteroid(self.position.x + offset2.x, self.position.y + offset2.y, new_radius)
        new_asteroid2.velocity = new_velocity2 * 50  

        for container in Asteroid.containers:
            container.add(new_asteroid1)
            container.add(new_asteroid2)

        # Wipe out the old asteroid
        self.kill()