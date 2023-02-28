# Main program that keeps all the changes made along the way while going through each TIY exercise.
import sys
import pygame
from game_character import Princess

class TIY:
    """Simple game task to practice what the book has already explained."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        self.bg_color = (135,206,235)

        pygame.display.set_caption("TIY GAME")

        self.princess = Princess(self)

    def run_game(self):
        """Start of the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.princess.blitme()
            
            pygame.display.flip()


if __name__=='__main__':
    tiy = TIY()
    tiy.run_game()