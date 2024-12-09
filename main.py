import pygame
from constants import *
from player import Player
from circleshape import CircleShape

# Initialize Pygame
pygame.init()

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')

dt = 0    

# Set up the display
pygame.display.set_caption("Asteroids")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a player
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Create a clock object for the frame rate control
clock = pygame.time.Clock()

# Game loop
run = True
while run:
    
    dt = clock.tick(60) / 1000    # Calculate delta time before updates
    
    screen.fill((0, 0, 0))    # RGB for black
      
    player.draw(screen)
    player.update(dt) 
    
    # Handle events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    
    # Refresh the screen        
    pygame.display.flip()

    


if __name__ == "__main__":
    main()