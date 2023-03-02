import pygame
from pygame.sprite import Sprite

class Cloud(Sprite):
    """A class to represent a single cloud in a storm"""
    
    def __init__(self, rd_scene):
        """Initialization of the cloud and set its starting position"""
        super().__init__()
        self.screen = rd_scene.screen
        self.settings = rd_scene.settings

        # Load the cloud image and set its rect attributes
        self.image = pygame.image.load('Chapter13_Aliens\Raindrops\cloud.png')
        self.rect = self.image.get_rect()

        # Starting point for clouds at top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the cloud's exact x_pos
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if row of clouds hits edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.left >= screen_rect.right or self.rect.right <0:
            return True
        
    def update(self):
        """Move the clouds to the right"""
        self.x += (self.settings.cloud_speed * self.settings.cloud_direction)
        self.rect.x = self.x 
    