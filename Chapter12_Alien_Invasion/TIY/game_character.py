# 12-2 Game character
    # Find a bitmap image of a game character and convert an image to a bitmap.
    # Make a class that draws the character at the center of the screen and match the background color of the image to the background color of the screen. 
        # Converted using https://cloudconvert.com/png-to-bmp

import pygame

class Princess:
    """A class to manage the princess's assets."""

    def __init__(self, tiy_game):
        """Initialization and set starting position."""
        self.screen = tiy_game.screen
        self.screen_rect = tiy_game.screen.get_rect()

        #Load the princess and get its rectangle.
        self.image = pygame.image.load('Chapter12_Alien_Invasion/TIY/princess.bmp')
        self.rect = self.image.get_rect()

        # Start position 
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the princess at her current location."""
        self.screen.blit(self.image, self.rect)

# Ready to be imported in tiy_game and placed in the __init__ as well as run_game functions. 