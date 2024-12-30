import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Initialize Pygame
pygame.init()

# Initialize font module
pygame.font.init()
font = pygame.font.Font(None, 74)  # Default font, size 74
small_font = pygame.font.Font(None, 36)  # Smaller font for instructions

def draw_text(screen, text, font, color, position):
    """Helper function to draw text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def show_start_screen(screen):
    """Function to display the start screen."""
    screen.fill((0, 0, 0))  # Fill the screen with black
    draw_text(screen, "Asteroids", font, (255, 0, 0), (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
    draw_text(screen, "Press any key to start", small_font, (255, 255, 255), (SCREEN_WIDTH // 2 - 155, SCREEN_HEIGHT // 2 + 20))
    pygame.display.flip()  # Refresh the screen

    # Wait for any key press to start the game
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                waiting = False

    return True

def main():
    while True:
        print("Starting asteroids!")
        print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')   

        # Set up the display
        pygame.display.set_caption("Asteroids")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Show the start screen
        if not show_start_screen(screen):
            break  # Exit if the user quits

        # Create sprites
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        #new_asteroid = pygame.sprite.Group()
        shoots = pygame.sprite.Group()

        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable)
        Shot.containers = (shoots, updatable, drawable)

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        asteroid_field = AsteroidField()    # spawns a new Asteroid
        
        
        drawable.add(player)
        updatable.add(player)
        updatable.add(asteroid_field)

        # Create a clock object for frame rate control
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

            # Check for collisions between asteroids
            for sprite in asteroids:
                for other in asteroids:
                    if sprite != other and sprite.collide(other):
                            sprite.kill()    # asteroids wipe out
                            other.kill()
            
            # Bullet destroys asteroids
            for sprite in asteroids:
                for bullet in shoots:
                    if sprite.collide(bullet):
                        sprite.split()    # asteroid splits
                        bullet.kill()    # bullet wipe out
                        
            # Check for collisions between player and asteroids
            for asteroid in asteroids:
                if player.collide(asteroid):
                    print("GAME OVER!")
                    run = False
            
            # Handle events
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return  # Exit the game
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_q:  # Press 'Q' to quit
                        return
            
            # Refresh the screen        
            pygame.display.flip()

        # Game over loop
        game_over = True
        while game_over:
            screen.fill((0, 0, 0))  # Clear screen before drawing text
            
            draw_text(screen, "GAME OVER!", font, (255, 0, 0), (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 50))
            draw_text(screen, "Press 'R' to restart", small_font, (255, 255, 255), (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 20))
            draw_text(screen, "Press 'Q' to quit", small_font, (255, 255, 255), (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 60))

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_r:  # Press 'R' to restart
                        game_over = False  # Break out of the game-over loop to restart
                    if e.key == pygame.K_q:  # Press 'Q' to quit
                        return

            pygame.display.flip()  # Refresh the screen during game over loop

if __name__ == "__main__":
    main()
