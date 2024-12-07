import pygame
from constants import *

# Initialize Pygame
pygame.init()    

# Set up the display
pygame.display.set_caption("Asteroids")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game loop
run = True
while run:
    # Fill the screen with black color
    screen.fill((0, 0, 0))    # RGB for black
    
    
    # Handle events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    
    # Refresh the screen        
    pygame.display.flip()

def main():
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')    
if __name__ == "__main__":
    main()