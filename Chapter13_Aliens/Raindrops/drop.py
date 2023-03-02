# Program to handle all assets and behavior related to the rain
import pygame
from pygame.sprite import Sprite

class Drop(Sprite):

    def __init__(self, rd_scene):
        super().__init__()
        self.screen = rd_scene.screen
        self.settings = rd_scene.settings

        self.image = pygame.image.load('Chapter13_Aliens/Raindrops/raindrop.png')
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        self.y += (self.settings.drop_speed)
        self.rect.y = self.y
        
