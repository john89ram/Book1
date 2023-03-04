import pygame
from pygame.sprite import Sprite
from random import randint

class Enemy(Sprite):
    """Class to represent a single enemy in game"""

    def __init__(self, tp_game):
        """Initialize the enemy in game and set starting pos"""
        super().__init__()
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = tp_game.settings

        self.image = pygame.image.load('Chapter14_Scoring/Target_Practice2/images/target.png')
        self.rect = self.image.get_rect()

        self.rect.right = self.screen_rect.right
        self.rect.y = randint(200,600)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top <0 or self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        self.speed = self.settings.enemy_speed

        #Change to y movement once confirmed
        self.y += (self.speed * self.settings.enemy_direction)
        self.rect.y = self.y
        