# File to handle bullet assets

import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    """Class to manage bullets fired from cowboy"""

    def __init__(self, ss_game):
        """Create a bullet object at the cowboy's location"""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = ss_game.settings.bullet_color

        self.rect = pygame.Rect(0,0, self.settings.bullet_w, 
                                self.settings.bullet_h)
        self.rect.midright = ss_game.cowboy.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen"""
        self.x += self.settings.bullet_s

        self.rect.x = self.x

    def draw_bullet(self):
        """Drawing bullets on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)