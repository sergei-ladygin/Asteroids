
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
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
        
            # Create first new asteroid
            new_velocity1 = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).rotate(0)
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = new_velocity1 * 1.2
            for container in Asteroid.containers:
                container.add(new_asteroid1)
        
            # Create second new asteroid
            new_velocity2 = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).rotate(180)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = new_velocity2 * 1.2
            for container in Asteroid.containers:
                container.add(new_asteroid2)