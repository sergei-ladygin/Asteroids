import pygame
from constants import *
from player import Player
from circleshape import CircleShape

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()
dt = 0    

# Set up the display
pygame.display.set_caption("Asteroids")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a player
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Game loop
run = True
while run:
    # Fill the screen with black color
    screen.fill((0, 0, 0))    # RGB for black
    
    
    player.draw(screen) 
    
    # Handle events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        clock.tick(60)
    dt = clock.tick() / 1000
    
    # Refresh the screen        
    pygame.display.flip()

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')    


if __name__ == "__main__":
    main()