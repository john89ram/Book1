# cowboy.py
# Program to handle the cowboy assets
import pygame

class Cowboy:
    """Class to manage the cowboy"""

    def __init__(self, ss_game):
        """Initialize"""
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()
        self.settings = ss_game.settings

        self.image = pygame.image.load('Chapter12_Alien_Invasion/TIY/SideShooter/cowboy.png')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the cowboy's position based on the movement flags"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.cowboy_s
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.cowboy_s

        self.rect.y = self.y

    def blitme(self):
        """Draw the cowboy at its current location."""
        self.screen.blit(self.image, self.rect)