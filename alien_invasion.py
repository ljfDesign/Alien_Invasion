import sys
import pygame

def run_game():

    # initialize game and creat a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien_Invasion")

    # Set the background color.
    bg_color = (230, 230, 230)

    # Start the main loop for the game.
    while True:

        # Watch for Keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through loop.
        screen.fill(bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
