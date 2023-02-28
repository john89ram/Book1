# 12-1 Blue Sky
    # Make a pygame window with a blue background.

import sys
import pygame

class TIY_Game:
    """Simple game task to practice what the book has already explained."""

    # Always needs to initialize the game.
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # Creating the game window size (measured by pixels)
        self.screen = pygame.display.set_mode((800,800))
        #Setting the background to blue
        self.bg_color = (135,206,235)
        # Creates a title on the window bar
        pygame.display.set_caption("TIY GAME")

    # Lets have a while loop to keep the game constantly running.
    def run_game(self):
        """Start of the main loop for the game."""
        while True:
            # Looks for all event types in pygame.events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # If the 'x' or QUIT is selected the system exits the game. (closes the window and ends the program.)
                    sys.exit()
            # Set the main game to fill the background to what we dictated above in init
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__=='__main__':
    # Creating a instance of the game to use all that we have created above.
    tiy_game = TIY_Game()
    # Here we can run the while loop/main game.
    tiy_game.run_game()