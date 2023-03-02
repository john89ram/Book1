import pygame
from pygame.sprite import Sprite
from random import randint

class Snake(Sprite):
    """Class to represent a single snake in a swarm"""

    def __init__(self, ss_game):
        """Initialize the snake and set its starting pos"""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        #Load the snake image and set its rect
        self.image = pygame.image.load('Chapter13_Aliens/Sideshooter2/snake-smaller.png')
        self.rect = self.image.get_rect()

        # Start each new snake pos
        self.rect.x = 1150
        self.rect.y = randint(75, 675)

        # Store the exact x pos
        self.x = float(self.rect.x)

    def update(self):
        self.x -= (self.settings.snake_speed)
        self.rect.x = self.x