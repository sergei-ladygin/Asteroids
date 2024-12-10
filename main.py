import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


# Initialize Pygame
pygame.init()

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')   

# Set up the display
pygame.display.set_caption("Asteroids")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create sprites
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()    # spawns a new Asteroid

updatable.add(player)
updatable.add(asteroid_field)
drawable.add(player)

# Create a clock object for the frame rate control
clock = pygame.time.Clock()

# Game loop
run = True
while run:
    
    dt = clock.tick(60) / 1000    # Calculate delta time before updates
    
    screen.fill((0, 0, 0))    # RGB for black
    
    for sprite in drawable:
        sprite.draw(screen)
    for sprite in updatable:    
        sprite.update(dt)
    
    # Handle events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    
    # Refresh the screen        
    pygame.display.flip()

    


if __name__ == "__main__":
    main()