import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    
    cooldown_timer = 0
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) 
        self.rotation = 0
        self.cooldown_timer = 0
        
    def triangle(self):
        # Create a triangle pointing forward, with the tip at the player's position    
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 4)
        
    def update(self, dt):
        keys = pygame.key.get_pressed()       

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt) 
        if keys[pygame.K_SPACE] and self.cooldown_timer <= 0:
            self.shoot()
            
        # Decrement the cooldown timer
        if self.cooldown_timer > 0:
            self.cooldown_timer -= dt
            
            
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.cooldown_timer = PLAYER_SHOOT_COOLDOWN
        